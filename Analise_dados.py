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



total_ev= dados.groupby(["stroke","ever_married"])["ever_married"].count()
total_wt= dados.groupby(["stroke","work_type"])["work_type"].count()
total_rt= dados.groupby(["stroke","Residence_type"])["Residence_type"].count()

#print(total_ev)
#print(total_wt)
#print(total_rt)

percentual_ev=(total_ev/total_avc * 100).round(2)
percentual_wt=(total_wt/total_avc * 100).round(2)
percentual_rt=(total_rt/total_avc * 100).round(2)
print(percentual_ev)
print(percentual_wt)
print(percentual_rt)






