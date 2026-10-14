# Análise de Dados de Saúde

## 1. Introdução

Este trabalho apresenta uma análise de dados de saúde com foco na comparação entre pacientes com e sem ocorrência de AVC. A análise foi desenvolvida em Python utilizando Pandas para preparação e exploração dos dados, Matplotlib para visualização e SQLite para armazenamento e consultas.

O objetivo foi identificar diferenças observadas entre os dois grupos em características como idade, hipertensão, doença cardíaca, nível médio de glicose, IMC e tabagismo. Os resultados representam apenas o comportamento do conjunto de dados analisado e não devem ser interpretados como relações de causa e efeito.

## 2. Preparação e tratamento dos dados

O arquivo original `Atividade2.csv` possui 5.110 registros e 12 colunas:

`id`, `gender`, `age`, `hypertension`, `heart_disease`, `ever_married`, `work_type`, `Residence_type`, `avg_glucose_level`, `bmi`, `smoking_status` e `stroke`.

A verificação de valores ausentes mostrou que somente a coluna `bmi` apresentava dados faltantes, totalizando 201 registros. Esses valores foram preenchidos com a média da própria coluna, utilizando `fillna()`.

Após o tratamento, foi realizada uma nova verificação para confirmar que não restavam valores ausentes. O conjunto tratado foi salvo em `Atividade2_tratado.csv`, mantendo o arquivo original preservado.

## 3. Análise exploratória

Dos 5.110 pacientes, 4.861 não apresentaram AVC e 249 apresentaram AVC.

### Idade

A idade média dos pacientes sem AVC foi de 41,97 anos, enquanto a média do grupo com AVC foi de 67,73 anos. As medianas foram, respectivamente, 43 e 71 anos.

Entre os pacientes com AVC, a distribuição por faixa etária foi:

- 0 a 17 anos: 2 pacientes (0,80%);
- 18 a 39 anos: 6 pacientes (2,41%);
- 40 a 59 anos: 60 pacientes (24,10%);
- 60 anos ou mais: 181 pacientes (72,69%).

Dentro deste conjunto de dados, observa-se uma concentração muito maior de pacientes com AVC na faixa de 60 anos ou mais.

### Hipertensão

Entre os pacientes sem AVC, 8,89% apresentavam hipertensão. Entre os pacientes com AVC, esse percentual foi de 26,51%.

A proporção de hipertensão foi maior no grupo com AVC, porém essa diferença representa apenas uma associação observada nos dados.

### Doença cardíaca

A presença de doença cardíaca foi observada em 4,71% dos pacientes sem AVC e em 18,88% dos pacientes com AVC.

Assim como na hipertensão, a proporção foi maior entre os pacientes com AVC no conjunto analisado.

### Nível médio de glicose

A média do nível de glicose foi de 104,80 no grupo sem AVC e de 132,54 no grupo com AVC. As medianas foram 91,47 e 105,22, respectivamente.

O grupo com AVC apresentou valores médios mais elevados. A diferença entre média e mediana também indica que valores altos de glicose influenciam a média.

### IMC

O IMC médio foi de 28,83 entre os pacientes sem AVC e 30,22 entre os pacientes com AVC. As medianas foram 28,30 e 28,89.

A diferença observada no IMC foi menor do que as diferenças encontradas em idade, hipertensão, doença cardíaca e glicose.

### Tabagismo

No grupo sem AVC, 16,77% eram ex-fumantes, 15,37% fumavam atualmente, 37,07% nunca fumaram e 30,80% estavam classificados como `Unknown`.

No grupo com AVC, 28,11% eram ex-fumantes, 16,87% fumavam atualmente, 36,14% nunca fumaram e 18,88% estavam classificados como `Unknown`.

A maior diferença entre os grupos ocorreu na categoria de ex-fumantes. A proporção de fumantes atuais foi relativamente próxima.

## 4. Visualizações

### Gráfico 1 — Faixa etária dos pacientes com AVC

**Arquivo:** `graficos/Faixa_etaria.png`

O gráfico mostra a distribuição absoluta dos pacientes com AVC por faixa etária. Dos 249 pacientes com AVC, 181 tinham 60 anos ou mais, correspondendo a 72,69% do grupo.

Esse resultado reforça a diferença observada na análise de idade: no conjunto analisado, os casos de AVC estão concentrados principalmente nas faixas etárias mais altas.

> Inserir aqui a imagem `graficos/Faixa_etaria.png`.

### Gráfico 2 — Hipertensão em pacientes com e sem AVC

**Arquivo:** `graficos/Hipertensao.png`

A hipertensão foi escolhida para o segundo gráfico por apresentar uma diferença clara entre os grupos. Entre os pacientes sem AVC, 8,89% apresentavam hipertensão, enquanto entre os pacientes com AVC o valor foi de 26,51%.

A utilização de percentuais é importante porque os dois grupos possuem tamanhos muito diferentes: 4.861 pacientes sem AVC e 249 com AVC.

> Inserir aqui a imagem `graficos/Hipertensao.png`.

### Gráfico 3 — Estado civil dos pacientes com e sem AVC

**Arquivo principal:** `graficos/Estado_civil_percentual.png`

Entre os pacientes sem AVC, 64,45% eram casados e 35,55% não eram casados. Entre os pacientes com AVC, 88,35% eram casados e 11,65% não eram casados.

Existe uma diferença considerável entre os grupos, mas ela não permite concluir que o estado civil tenha relação causal com o AVC. Uma possível influência é a idade, pois o grupo com AVC possui idade média significativamente maior e pessoas mais velhas também podem apresentar maior frequência de casamento.

> Inserir aqui a imagem `graficos/Estado_civil_percentual.png`.

## 5. Armazenamento e consultas com SQLite

Após o tratamento, os dados foram armazenados em um banco SQLite chamado `dados_saude.db`. A tabela criada recebeu o nome `pacientes` e contém os 5.110 registros do arquivo tratado.

Foram realizadas três consultas principais:

### Consulta 1 — Total de registros

Resultado: **5.110 registros**.

### Consulta 2 — Pacientes com AVC

Resultado: **249 pacientes** com `stroke = 1`.

### Consulta 3 — Média de glicose por grupo

Resultados:

- Sem AVC: **104,80**;
- Com AVC: **132,54**.

Os resultados obtidos no SQLite foram compatíveis com os valores encontrados anteriormente utilizando Pandas.

## 6. Conclusão

A análise mostrou diferenças relevantes entre pacientes com e sem AVC dentro do conjunto de dados estudado. O grupo com AVC apresentou idade média mais elevada, maior proporção de hipertensão e doença cardíaca e maior nível médio de glicose.

A maior parte dos pacientes com AVC possuía 60 anos ou mais. Também foram observadas diferenças em características como estado civil e histórico de tabagismo. Entretanto, essas diferenças devem ser interpretadas apenas como associações presentes neste conjunto de dados, sem afirmar causalidade.

O uso de Pandas permitiu realizar a preparação, o tratamento e a análise exploratória; o Matplotlib foi utilizado para representar os resultados graficamente; e o SQLite permitiu armazenar os dados tratados e realizar consultas diretamente no banco.
