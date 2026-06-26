import time

inicio = time.time()

with open("dados.txt") as arq:
    numeros = [int(x) for x in arq]

numeros.sort()

fim = time.time()

print(
    "Tempo Python sort:",
    round(fim-inicio,2),
    "segundos"
)
