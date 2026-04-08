from inferencia.executar_inferencia import run_mcq, run_abertas
from metricas.avaliar_multiplas import avaliar as eval_mcq
from metricas.avaliar_abertas import avaliar as eval_abertas

isTest = True

print("1. Inferência\n")
run_abertas(isTest)
run_mcq(isTest)

print("2. Avaliação\n")
eval_abertas(isTest)
eval_mcq(isTest)

print("FIM - TESTE")