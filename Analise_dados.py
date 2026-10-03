import pandas as pd
import matplotlib.pyplot as plt

dados=pd.read_csv("Atividade2_tratado.csv")

total_avc = dados.groupby("stroke")["stroke"].count()
#print(total_avc)

# 4861 sem AVC
# 249 tiveram AVC




idade_minima_avc = dados[dados["stroke"] == 1]["age"].min()
idade_maxima_avc = dados[dados["stroke"] == 1]["age"].max()
"""
print(idade_minima_avc)
#1.32 anos
print(idade_maxima_avc)
#82 anos
"""


#Informação idade COM e SEM AVC

media_idade_avc= dados.groupby("stroke")[["age","avg_glucose_level","bmi"]].mean().round(2)
mediana_idade_avc= dados.groupby("stroke")[["age","avg_glucose_level","bmi"]].median().round(2)
#print(media_idade_avc) 
#print("\n") 
#print(mediana_idade_avc)

#### Criando nova coluna para separar por categoria de idade 
# aula 16 para criar a coluna e 17 para mudar os valores

dados["faixa_etaria"] = ""

dados.loc[dados["age"] < 18, "faixa_etaria"] = "0-17"

dados.loc[(dados["age"] >= 18) & (dados["age"] < 40),"faixa_etaria"] = "18-39"

dados.loc[ (dados["age"] >= 40) & (dados["age"] < 60), "faixa_etaria"] = "40-59"

dados.loc[dados["age"] >= 60, "faixa_etaria"] = "60+"

##calcula o total por faixa etaria (valores absolutos)
total_fe= dados.groupby(["stroke","faixa_etaria"] )["faixa_etaria"].count()
print(total_fe)
# stroke  faixa_etaria
# 0       0-17             854
#         18-39           1308
#         40-59           1504
#         60+             1195

# 1       0-17               2
#         18-39              6
#         40-59             60
#         60+              181


##calcula o total por faixa etaria (%)
percentual_fe=(total_fe/total_avc * 100).round(2)
print(percentual_fe)

# Name: faixa_etaria, dtype: int64
# stroke  faixa_etaria

# 0       0-17            17.57
#         18-39           26.91
#         40-59           30.94
#         60+             24.58

# 1       0-17             0.80
#         18-39            2.41
#         40-59           24.10
#         60+             72.69






# ele só vai somar os 1 para COM e SEM AVC, ou seja ai me mostra todo mundo que tem e se eu quiser qm n tem eu subtraio do valor tota.
# NÃO É O TOTAL GERAL E SIM O TOTAL DE PESSOAS COM AQUELE PROBLEMA OU SEJA: DE 4861 PESSOAS SEM AVC 432 TEM HIPERTENSÃO E 229 TEM PROBLEMAS CARDIACOS
# LOGO DE 249 PESSOAS COM AVC 66 TEM HIPERTENSÃO E 47 TEM PROBLEMAS CARDIACOS

# Hipertensão(hp)
#        hypertension
#stroke              
#0                432
#1                 66

total_hp= dados.groupby("stroke")["hypertension"].sum()
#print(total_hp)


#Problemas Cardiacos (pc)
# heart_disease
#stroke               
#0                 229
#1                  47
total_pc= dados.groupby("stroke")["heart_disease"].sum()
#print(total_pc)


# PC e HP em %
percentual_hp = (total_hp / total_avc * 100).round(2)
percentual_pc = (total_pc / total_avc * 100).round(2)
#print("% de pessoas com hipertensão", percentual_hp)
#print("% de pessoas com problemas cardiacos",percentual_pc)


# calculo fumantes e não fumantes status (fs)
# aula 18 slide 10, agrupamento por categoria
total_fs= dados.groupby(["stroke","smoking_status"])["smoking_status"].count()

#print(total_fs)

#      stroke  smoking_status 
#      0-4861  Unknown            1497
#              formerly smoked     815
#              never smoked       1802
#              smokes              747
#      1-249   Unknown              47
#              formerly smoked      70
#              never smoked         90
#              smokes               42

# % de fumantes e não fumantes
percentual_fs = (total_fs / total_avc * 100).round(2)
#print(percentual_fs)

#stroke  smoking_status 
#0       Unknown            30.80    
#        formerly smoked    16.77   
#        never smoked       37.07
#        smokes             15.37

#1       Unknown            18.88
#        formerly smoked    28.11
#        never smoked       36.14
#        smokes             16.87

## total por genero

total_gn= dados.groupby(["stroke","gender"])["gender"].count()
#print(total_gn)

#stroke  gender
#0       Female    2853
#        Male      2007
#        Other        1
#1       Female     141
#        Male       108

## % por genero

percentual_gn=(total_gn/total_avc * 100).round(2)
#print(percentual_gn)

#0       Female    58.69
#        Male      41.29
#        Other      0.02
#1       Female    56.63
#        Male      43.37


## valores não obrigatoriso (casado, lugar onde mora, trablho)
total_ev= dados.groupby(["stroke","ever_married"])["ever_married"].count()
total_wt= dados.groupby(["stroke","work_type"])["work_type"].count()
total_rt= dados.groupby(["stroke","Residence_type"])["Residence_type"].count()
# print(total_ev)
# print(total_wt)
# print(total_rt)
# stroke  ever_married
# 0       No              1728
#         Yes             3133
# 1       No                29
#         Yes              220


# Name: ever_married, 
# stroke  work_type    
# 0       Govt_job          624
#         Never_worked       22
#         Private          2776
#         Self-employed     754
#         children          685
# 1       Govt_job           33
#         Private           149
#         Self-employed      65
#         children            2


# Name: work_type,
# stroke  Residence_type
# 0       Rural             2400
#         Urban             2461
# 1       Rural              114
#         Urban              135


percentual_ev=(total_ev/total_avc * 100).round(2)
percentual_wt=(total_wt/total_avc * 100).round(2)
percentual_rt=(total_rt/total_avc * 100).round(2)
# print(percentual_ev)
# print(percentual_wt)
# print(percentual_rt)

# stroke  ever_married
# 0       No              35.55
#         Yes             64.45
# 1       No              11.65
#         Yes             88.35


# stroke  work_type    
# 0       Govt_job         12.84
#         Never_worked      0.45
#         Private          57.11
#         Self-employed    15.51
#         children         14.09
# 1       Govt_job         13.25
#         Private          59.84
#         Self-employed    26.10
#         children          0.80


# stroke  Residence_type
# 0       Rural             49.37
#         Urban             50.63
# 1       Rural             45.78
#         Urban             54.22



## dados complementares ################################################

#PARTE 1 AVC, HIPERTENSÃO E PROBLEMA CARDIACO

#valores totais
total_hp_pc_avc= dados.groupby(["stroke","hypertension","heart_disease"])["stroke"].count()
#print(total_hp_pc_avc)

# 0       0             0                4251
#                       1                 178
#         1             0                 381
#                       1                  51
# 1       0             0                 149
#                       1                  34
#         1             0                  53
#                       1                  13

#valores em %
percentual_hp_pc_avc = (total_hp_pc_avc/total_avc * 100).round(2)
#print(percentual_hp_pc_avc)

# stroke  hypertension  heart_disease
# 0       0             0                87.45
#                       1                 3.66
#         1             0                 7.84
#                       1                 1.05

# 1       0             0                59.84
#                       1                13.65
#         1             0                21.29
#                       1                 5.22



