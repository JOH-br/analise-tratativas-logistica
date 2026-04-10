import sqlite3

# conecta no banco
conn = sqlite3.connect("../database/tratativas.db")
cursor = conn.cursor()

# lê e executa queries.sql
with open("../sql/queries.sql", "r") as f:
    query = f.read()

cursor.execute(query)

# pega resultados
resultados = cursor.fetchall()

# mostra no terminal
for linha in resultados:
    print(linha)

conn.close()