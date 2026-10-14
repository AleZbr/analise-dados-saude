# Análise de Dados de Saúde

Projeto acadêmico desenvolvido em Python para preparação, tratamento, análise, visualização e armazenamento de dados de saúde, com foco na comparação entre pacientes com e sem AVC.

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- SQLite

## Estrutura do projeto

```text
.
├── Analise_dados.py
├── Verificacao_dados.py
├── banco_dados.py
├── Atividade2.csv
├── Atividade2_tratado.csv
├── dados_saude.db
├── graficos/
│   ├── AVC.png
│   ├── Faixa_etaria.png
│   ├── Faixa_etaria_%.png
│   ├── Hipertensao.png
│   ├── Problema_cardiaco.png
│   ├── Glicose.png
│   ├── IMC.png
│   ├── Tabagismo.png
│   ├── Estado_civil_total.png
│   └── Estado_civil_percentual.png
└── README.md
```

## Preparação dos dados

O conjunto original possui 5.110 registros e 12 colunas. Durante a verificação foram encontrados 201 valores ausentes na coluna `bmi`.

Os valores ausentes foram preenchidos com a média do IMC e o resultado foi salvo em `Atividade2_tratado.csv`, mantendo o arquivo original preservado.

## Análise exploratória

A análise compara pacientes com e sem AVC em diferentes características, incluindo:

- idade e faixa etária;
- hipertensão;
- doença cardíaca;
- nível médio de glicose;
- IMC;
- tabagismo;
- gênero;
- estado civil;
- tipo de trabalho;
- tipo de residência.

A base possui:

- **4.861 pacientes sem AVC**
- **249 pacientes com AVC**

Alguns resultados observados:

| Característica | Sem AVC | Com AVC |
|---|---:|---:|
| Idade média | 41,97 | 67,73 |
| Glicose média | 104,80 | 132,54 |
| IMC médio | 28,83 | 30,22 |
| Hipertensão | 8,89% | 26,51% |
| Doença cardíaca | 4,71% | 18,88% |

Os resultados representam associações observadas neste conjunto de dados e não indicam causalidade.

## Gráficos

Os gráficos gerados pelo projeto são armazenados na pasta `graficos/`.

Entre as principais visualizações estão:

- distribuição por faixa etária dos pacientes com AVC;
- comparação de hipertensão entre pacientes com e sem AVC;
- comparação de doença cardíaca, glicose, IMC e tabagismo;
- comparação do estado civil entre pacientes com e sem AVC.

## SQLite

Os dados tratados são armazenados no banco:

```text
dados_saude.db
```

A tabela utilizada é:

```text
pacientes
```

Foram implementadas consultas para:

1. contar o total de registros armazenados;
2. contar os pacientes com AVC;
3. comparar a média de glicose entre pacientes com e sem AVC.

Resultados principais:

```text
Total de registros: 5110
Pacientes com AVC: 249
Média de glicose:
[(0, 104.8), (1, 132.54)]
```

## Como executar

Instale as bibliotecas necessárias:

```bash
pip install pandas matplotlib
```

Execute a preparação dos dados:

```bash
python Verificacao_dados.py
```

Execute a análise e gere os gráficos:

```bash
python Analise_dados.py
```

Execute a criação e as consultas do banco SQLite:

```bash
python banco_dados.py
```

## Observação

Este projeto possui finalidade acadêmica. As diferenças encontradas representam somente o conjunto de dados analisado e não devem ser interpretadas como relações de causa e efeito.
