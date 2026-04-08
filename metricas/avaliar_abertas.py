import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

def avaliar(isTest):
    data = json.load(open("resultados/resultados_abertas.json"))
    
    if isTest:
        data = json.load(open("resultados/resultados_abertas_teste.json"))

    modelos = [k for k in data[0] if k not in ["question", "reference_answer"]]

    final = []
    i=0
    for answer in data :
        linha = {}
        question = answer["question"]
        linha = {"question": question,}
        reference = answer["reference_answer"] or ""
        i = i+1
        print("Pergunta ",i, ": ", question,"\n ")
        for m in modelos:
            candidate = answer.get(m, "")

            if not candidate:
                print("Candidate not found","\n ")
                linha[m] = "Candidate not found"
                continue
            
            result = score(candidate, reference)
            print("Nota: ", result[0],"\n ")
            linha[m] = {
                "result": result[0],
            }
        final.append(linha)
        
    path = "metricas/metricas_abertas.json"
    
    if isTest:
        path = "metricas/metricas_abertas_teste.json"
    
    json.dump(final, open(path, "w"), indent=2)
    

    print("Fim avaliação abertas\n", final,"\n ")
    
def score(candidate, reference):
    
    print("Iniciando inferencia de avaliação","\n ")
    
    API_URL = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2/pipeline/sentence-similarity"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    
    payload = {
        "inputs": {
            "source_sentence": reference,
            "sentences": [candidate]
        },
    }
    
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=(5, 60)
        )

        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.ReadTimeout:
        print(f"Tentativa falhou por timeout...","\n ")
        return [{"error": "Timeout"}]
    
    except requests.exceptions.RequestException as e:
        return [{"error": str(e)}]