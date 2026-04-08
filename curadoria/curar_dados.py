import json
from curadoria.classificar import classificar_mcq, classificar_aberta

def curar_mcq():
    print("Curando multipla escolha...\n")
    #abre o arquivo e coloca na variavel data
    data = json.load(open("dados/brutos/multiplas_escolhas.json"))

    #declara variavel de saida que inicialmente é vazia
    out = []

    #for i in data:
    i = data[0]
    area, dif, ref = classificar_mcq(i["question"])

    out.append({
        **i,
        "area": area,
        "difficulty": dif,
        "reference": ref
    })

    json.dump(out, open("dados/curados/mcq_curado.json", "w"), indent=2)
    print("MCQ pronto\n")


def curar_abertas():
    print("Curando abertas\n")
    
    data = json.load(open("dados/brutos/questoes_abertas.json"))
    
    out = []

    #for i in data:
    i = data[0]

    q = i.get("Question") or i.get("question")

    area, dif, ref = classificar_aberta(q)

    out.append({
        "question": q,
        "reference_answer": i.get("Free_form_answer"),
        "area": area,
        "difficulty": dif,
        "reference": ref
    })

    json.dump(out, open("dados/curados/abertas_curado.json", "w"), indent=2)
    print("Abertas pronto\n")