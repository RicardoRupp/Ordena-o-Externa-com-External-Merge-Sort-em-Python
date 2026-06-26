# Ordenação Externa com External Merge Sort em Python

Projeto desenvolvido para pesquisa e implementação do algoritmo **External Merge Sort (Ordenação Externa por Intercalação)** utilizando Python.

O objetivo foi simular um cenário de processamento de grandes volumes de dados utilizando armazenamento em disco, comparando o desempenho da técnica de ordenação externa com o método nativo `sort()` do Python.

---

## Objetivo

Implementar e avaliar o algoritmo **External Merge Sort**, analisando seu comportamento em operações de ordenação com arquivos e comparando os resultados obtidos com métodos internos da linguagem.

---

## Tecnologias utilizadas

* Python 3
* Manipulação de arquivos (`.txt`)
* External Merge Sort
* Processamento em disco
* Medição de tempo de execução

---

## Estrutura do projeto

```plaintext
ordenacao-externa/
│
├── gerar_base.py
├── dados.txt
├── external_merge_sort.py
├── ordenado.txt
│
├── resultados/
│   ├── tempo_geracao.png
│   ├── tempo_merge.png
│   ├── tempo_sort.png
│   └── resultado_final.png
│
├── relatorio/
│   └── Relatorio_Final_Ordenacao_Externa.pdf
│
└── README.md
```

### Arquivos

| Arquivo                  | Descrição                                      |
| ------------------------ | ---------------------------------------------- |
| `gerar_base.py`          | Gera os dados simulados utilizados nos testes  |
| `dados.txt`              | Arquivo contendo os dados gerados              |
| `external_merge_sort.py` | Implementação do algoritmo External Merge Sort |
| `ordenado.txt`           | Arquivo contendo os dados ordenados            |
| `relatorio_final.pdf`    | Relatório completo do trabalho                 |

---

## Como funciona

O algoritmo segue as seguintes etapas:

1. Geração dos dados de entrada;
2. Leitura dos registros;
3. Ordenação dos blocos de dados;
4. Intercalação (*merge*) dos blocos ordenados;
5. Geração do arquivo final.

Fluxo do processo:

```plaintext
gerar_base.py
      ↓
dados.txt
      ↓
external_merge_sort.py
      ↓
ordenado.txt
```

---

## Como executar

### 1. Gerar os dados

Execute:

```bash
python gerar_base.py
```

Será criado:

```plaintext
dados.txt
```

---

### 2. Executar o algoritmo de ordenação

Execute:

```bash
python external_merge_sort.py
```

---

### 3. Verificar saída

Após a execução será gerado:

```plaintext
ordenado.txt
```

com todos os dados ordenados.

---

## Testes realizados

Foram realizados testes para medir o desempenho das diferentes etapas do projeto.

### Tempos obtidos

| Processo            | Tempo         |
| ------------------- | ------------- |
| Geração da base     | *(preencher)* |
| External Merge Sort | *(preencher)* |
| sort() do Python    | *(preencher)* |

> Os tempos podem variar conforme hardware, sistema operacional e volume de dados.

---

## Comparação

Foi realizada comparação entre:

* **External Merge Sort**
* **sort() do Python**

O método `sort()` apresentou referência para comparação em memória principal, enquanto o **External Merge Sort** foi utilizado para representar um cenário de ordenação externa baseada em arquivos.

---

## Evidências da execução

### Geração dos dados

```md
![Geração](resultados/tempo_geracao.png)
```

### External Merge Sort

```md
![Merge](resultados/tempo_merge.png)
```

### sort() do Python

```md
![Sort](resultados/tempo_sort.png)
```

### Resultado final

```md
![Resultado](resultados/resultado_final.png)
```

---

## Conceitos aplicados

* Ordenação Externa
* External Merge Sort
* Intercalação de Arquivos
* Manipulação de Dados
* Processamento em Disco
* Avaliação de Desempenho

---

## Relatório

O relatório completo do projeto está disponível em:

```plaintext
relatorio/Relatorio_Final_Ordenacao_Externa.pdf
```

---

## Autor
##Ricardo Rupp
**Ricardo Castelli Rupp**
Curso: Sistemas de Informação
