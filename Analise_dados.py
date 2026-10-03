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

total_hp= dados.groupby("stroke")[["hypertension"]].sum()
#print(total_hp)


#Problemas Cardiacos (pc)
# heart_disease
#stroke               
#0                 229
#1                  47
total_pc= dados.groupby("stroke")[["heart_disease"]].sum()
#print(total_pc)


# PC e HP em %



