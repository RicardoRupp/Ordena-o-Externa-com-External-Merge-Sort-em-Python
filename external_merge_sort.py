import os
import heapq
import time

PASTA_TEMP = "temp"
TAMANHO_BLOCO = 50000


def criar_blocos(arquivo):

    os.makedirs(PASTA_TEMP, exist_ok=True)

    blocos = []

    with open(arquivo, "r") as entrada:

        indice = 0

        while True:

            numeros = []

            for _ in range(TAMANHO_BLOCO):

                linha = entrada.readline()

                if not linha:
                    break

                numeros.append(int(linha))

            if not numeros:
                break

            numeros.sort()

            nome = f"{PASTA_TEMP}/chunk_{indice}.txt"

            with open(nome, "w") as temp:

                for valor in numeros:
                    temp.write(f"{valor}\n")

            blocos.append(nome)

            indice += 1

    return blocos


def intercalar(blocos, arquivo_saida):

    arquivos = [open(x) for x in blocos]

    heap = []

    for i, arq in enumerate(arquivos):

        linha = arq.readline()

        if linha:
            heapq.heappush(
                heap,
                (int(linha), i)
            )

    with open(arquivo_saida, "w") as saida:

        while heap:

            valor, origem = heapq.heappop(heap)

            saida.write(f"{valor}\n")

            linha = arquivos[origem].readline()

            if linha:
                heapq.heappush(
                    heap,
                    (int(linha), origem)
                )

    for arq in arquivos:
        arq.close()


inicio = time.time()

print("Criando blocos...")
blocos = criar_blocos("dados.txt")

print("Intercalando...")
intercalar(
    blocos,
    "ordenado.txt"
)

fim = time.time()

print()
print("Concluído")
print("Tempo:", round(fim - inicio, 2), "segundos")
