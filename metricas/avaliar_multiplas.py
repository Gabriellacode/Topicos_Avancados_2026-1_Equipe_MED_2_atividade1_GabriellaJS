import json

def avaliar(isTest):
    
    openPath = "resultados/resultados_mcq.json"
    if(isTest):
        openPath = "resultados/resultados_mcq_teste.json"
        
    try:
        with open(openPath, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Arquivo não encontrado!","\n ")
        return

    modelos = [k for k in data[0] if k not in ["question", "correct"]]
    
    acertos = {m: 0 for m in modelos}
    total = len(data)

    for item in data:
        for m in modelos:
            if str(item[m]).strip().upper() == str(item["correct"]).strip().upper():
                acertos[m] += 1

    # monta saída estruturada
    final = []
    for m in modelos:
        acuracia = 0 if total == 0 else round((acertos[m] / total) * 100, 4)
        final.append({
            "modelo": m,
            "acertos": acertos[m],
            "total": total,
            "acuracia": acuracia
        })

    # salva json
    
    path = "metricas/metricas_mcq.json"
    if isTest:
        path = "metricas/metricas_mcq_teste.json"
        
    with open(path, "w") as f:
        json.dump(final, f, indent=2)

    print("Fim avaliação multipla escolha")
