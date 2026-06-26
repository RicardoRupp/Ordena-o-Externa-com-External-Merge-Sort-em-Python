import random

QUANTIDADE = 500000
VALOR_MIN = 1
VALOR_MAX = 1000000
ARQUIVO = "dados.txt"

with open(ARQUIVO, "w") as arquivo:
    for _ in range(QUANTIDADE):
        arquivo.write(f"{random.randint(VALOR_MIN, VALOR_MAX)}\n")

print(f"Arquivo '{ARQUIVO}' gerado com {QUANTIDADE} registros.")
