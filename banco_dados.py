import pandas as pd
import sqlite3


# lê os dados já tratados
dados = pd.read_csv("Atividade2_tratado.csv")


# cria/conecta ao banco de dados
conexao = sqlite3.connect("dados_saude.db")


# cria a tabela e insere os dados do CSV
dados.to_sql(
    "pacientes",
    conexao,
    if_exists="replace",
    index=False
)


# cria o cursor para fazer as consultas SQL
cursor = conexao.cursor()


# CONSULTA 1 - total de registros armazenados
cursor.execute("SELECT COUNT(*) FROM pacientes")
total_registros = cursor.fetchone()[0]

print("Total de registros:", total_registros)


# CONSULTA 2 - quantidade de pacientes com AVC
cursor.execute("SELECT COUNT(*) FROM pacientes WHERE stroke = 1")
total_avc = cursor.fetchone()[0]

print("Pacientes com AVC:", total_avc)


# CONSULTA 3 - média de glicose de pacientes sem e com AVC
cursor.execute("""
    SELECT stroke, ROUND(AVG(avg_glucose_level), 2)
    FROM pacientes
    GROUP BY stroke
""")

media_glicose = cursor.fetchall()

print("Média de glicose:")
print(media_glicose)


# fecha a conexão
conexao.close()