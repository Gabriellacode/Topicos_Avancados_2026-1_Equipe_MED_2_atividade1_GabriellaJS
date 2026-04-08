import json
import requests
import re
from dotenv import load_dotenv
import os

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

MODELOS = {
   "llama": "meta-llama/Llama-3.2-1B-Instruct:novita",
   "qwen": "Qwen/Qwen3.5-27B:novita",
   "deep": "deepseek-ai/DeepSeek-R1:novita"
}

def chamar_modelo(modelo, prompt):

    API_URL = "https://router.huggingface.co/v1/chat/completions"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "model": modelo,
        "temperature": 0.5,
        "max_tokens": 1500
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=(5, 60)
        )

        response.raise_for_status()
        
        handled_respose = response.json()["choices"][0]["message"]["content"]
        if modelo == MODELOS["deep"]:
            handled_respose = extrair_resposta_deepseek(handled_respose)
        handled_respose = normalizar_espacos(handled_respose)
        print("Resposta: ", handled_respose, "\n")
        return handled_respose

    except requests.exceptions.ReadTimeout:
        print(f"Tentativa falhou por timeout...\n")
        return { "error": "Tentativa falhou por timeout..." }
    
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    
    
def carregar_prompt(path):
    return open(path).read()


def extrair_resposta_deepseek(texto: str) -> str:
    return re.sub(r'<think>.*?</think>', '', texto, flags=re.DOTALL)
def normalizar_espacos(texto: str) -> str:
    return re.sub(r'\s+', ' ', texto).strip()
def extrair_letra(texto: str) -> str:
    match = re.search(r'\b[A-E]\b',texto.upper())
    return match.group(0) if match else ''


def run_mcq(isTest):
    
    print("Inferencia multipla escolha\n")
    
    dados = json.load(open("dados/curados/mcq_curado.json"))
    if(isTest):
        dados = json.load(open("dados/curados/mcq_curado_teste.json"))
    prompt = carregar_prompt("prompts/prompt_mcq.txt")

    resultados = []

    i=0

    for d in dados:
        question = d["question"]
        p = prompt.format(question=question, options=d["options"])
        linha = {"question": d["question"], "correct": d["answer"]}
        
        print("Pergunta ", i, ": ",question,"\n ")
        i= i+1
        for nome, modelo in MODELOS.items():
            print("Chamando modelo ", nome,"\n ")
            linha[nome] = chamar_modelo(modelo, p)

        resultados.append(linha)

    path = "resultados/resultados_mcq.json"

    if isTest:
        path = "resultados/resultados_mcq_teste.json"
        

    json.dump(resultados, open(path, "w"), indent=2)
    print("MCQ rodado","\n ")


def run_abertas(isTest):
    
    print("Inferencia abertas","\n ")
    
    dados = json.load(open("dados/curados/abertas_curado.json"))
    
    if isTest :
        dados = json.load(open("dados/curados/abertas_curado_teste.json"))
    
    prompt = carregar_prompt("prompts/prompt_abertas.txt")

    resultados = []
    i=0;
    
    for d in dados:
        question = d["question"]
        p = prompt.format(question=question)

        linha = {
            "question": d["question"],
            "reference_answer": d["reference_answer"]
        }

        print("Pergunta ", i, ": ",question,"\n ")
        i = i+1

        for nome, modelo in MODELOS.items():
            print("Chamando modelo ", nome,"\n ")
            linha[nome] = chamar_modelo(modelo, p)

        resultados.append(linha)

    path = "resultados/resultados_abertas.json"
    
    if(isTest):
        path = "resultados/resultados_abertas_teste.json"
        
    
    json.dump(resultados, open(path, "w"), indent=2)
    print("Abertas rodado","\n ")