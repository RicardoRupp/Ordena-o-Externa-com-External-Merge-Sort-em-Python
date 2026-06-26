# Ordenação Externa com External Merge Sort em Python

Projeto desenvolvido para pesquisa e implementação do algoritmo **External Merge Sort (Ordenação Externa por Intercalação)** utilizando Python.

O trabalho teve como objetivo simular o processamento de grandes volumes de dados utilizando armazenamento em disco e comparar o desempenho da técnica de ordenação externa com o método nativo `sort()` do Python.

---

## Objetivo

Implementar e analisar o algoritmo **External Merge Sort**, avaliando seu comportamento em operações de ordenação com arquivos e comparando os resultados obtidos com o método interno de ordenação da linguagem Python.

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
├── external_merge_sort.py
├── comparacao.py
├── README.md
│
├── resultados/
│   ├── tempo_geracao.png
│   ├── tempo_merge.png
│   ├── tempo_sort.png
│   └── resultado_final.png
│
├── relatorio/
│   └── Relatorio_Final_Ordenacao_Externa.pdf
```

---

## Arquivos

| Arquivo                  | Descrição                                                             |
| ------------------------ | --------------------------------------------------------------------- |
| `gerar_base.py`          | Gera os dados simulados utilizados nos testes                         |
| `external_merge_sort.py` | Implementação do algoritmo External Merge Sort                        |
| `comparacao.py`          | Realiza comparação de desempenho entre External Merge Sort e `sort()` |
| `resultados/`            | Contém imagens e evidências dos testes                                |
| `relatorio/`             | Contém o relatório final do projeto                                   |
| `README.md`              | Documentação do projeto                                               |

---

## Como funciona

O algoritmo segue as seguintes etapas:

1. Geração da base de dados;
2. Leitura dos registros;
3. Divisão em partes menores;
4. Ordenação dos blocos;
5. Intercalação (*merge*);
6. Geração do arquivo final ordenado.

Fluxo simplificado:

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

Será criado o arquivo:

```plaintext
dados.txt
```

---

### 2. Executar a ordenação externa

Execute:

```bash
python external_merge_sort.py
```

Será gerado:

```plaintext
ordenado.txt
```

---

### 3. Executar comparação de desempenho

Execute:

```bash
python comparacao.py
```

O programa compara:

* External Merge Sort
* `sort()` do Python

---

## Testes realizados

Foram realizados testes para medir o desempenho das etapas do projeto.

### Resultados

| Processo            | Tempo         |
| ------------------- | ------------- |
| External Merge Sort | 2.79 segundos |
| sort() do Python    | 0.44 segundos |

> Os tempos podem variar conforme hardware e volume de dados.

---

## Comparação

Foi realizada comparação entre:

* **External Merge Sort**
* **sort() do Python**

O método `sort()` foi utilizado como referência de ordenação em memória principal, enquanto o **External Merge Sort** representa um cenário de processamento orientado a arquivos.

---

## Evidências da execução

### Tempo de geração da base

```md
![Tempo geração](resultados/tempo_geracao.png)
```

### Tempo — External Merge Sort

```md
![Merge](resultados/tempo_merge.png)
```

### Tempo — sort()

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
* Processamento em Disco
* Manipulação de Grandes Volumes de Dados
* Avaliação de Desempenho

---

## Relatório

O relatório completo do projeto está disponível em:

```plaintext
relatorio/Relatorio_Final_Ordenacao_Externa.pdf
```

---

## Autor

**Ricardo Castelli Rupp**
Curso: Sistemas de Informação
