from curadoria.curar_dados import curar_mcq, curar_abertas
from inferencia.executar_inferencia import run_mcq, run_abertas
from metricas.avaliar_multiplas import avaliar as eval_mcq
from metricas.avaliar_abertas import avaliar as eval_abertas

isTest = False
print("1. Curando\n")
curar_mcq()
curar_abertas()

print("2. Inferência\n")
run_abertas(isTest)
run_mcq(isTest)

print("3. Avaliação\n")
eval_abertas(isTest)
eval_mcq(isTest)

print("FIM - MAIN")