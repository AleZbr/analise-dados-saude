import pandas as pd
import matplotlib.pyplot as plt

dados=pd.read_csv("Atividade2.csv")


print(dados.shape[0])# 


print("#########")
print(dados.columns)
# como tratar a idade das crianças?????? esta tudo em anos

#total_genero = dados.groupby('gender', dropna=False).size()
#total_idade = dados.groupby('age', dropna=False).size()
#total_hipertensão = dados.groupby('hypertension', dropna=False).size()
#total_coração = dados.groupby('heart_disease', dropna=False).size()
#total_casado = dados.groupby('ever_married', dropna=False).size()
#total_trabalho = dados.groupby('work_type', dropna=False).size()
#total_residencia = dados.groupby('Residence_type', dropna=False).size()
#total_glicose = dados.groupby('avg_glucose_level', dropna=False).size()
#total_imc = dados.groupby('bmi', dropna=False).size()
#total_fumante = dados.groupby('smoking_status', dropna=False).size()
#total_AVC = dados.groupby('stroke', dropna=False).size()

#print(total_pessoas)
#print(total_genero)
#print(total_idade)#.to_string())
#print(total_hipertensão)
#print(total_coração)
#print(total_casado)
#print(total_trabalho)
#print(total_residencia)
#print(total_glicose)#.to_string())
#print(total_imc.to_string())
#print(total_fumante)
#print(total_AVC)



""" 
#verifica dados vazios
#print(dados.isnull().sum())
#calcula a media para os dados vazios
media_imc= dados["bmi"].mean()
#preenche os valores vazios
dados["bmi"] =(dados["bmi"].fillna(media_imc))
#verifica se ainda existe valorss nulos
print(dados.isnull().sum())
#cria o novo CSV sem dados nulos
dados.to_csv("Atividade2_tratado.csv", index=False)
"""