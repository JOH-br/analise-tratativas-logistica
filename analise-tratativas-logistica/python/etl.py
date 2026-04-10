import sqlite3

# conecta (cria o banco se não existir)
conn = sqlite3.connect("../database/tratativas.db")
cursor = conn.cursor()

# lê e executa create_tables.sql
with open("../sql/create_tables.sql", "r") as f:
    cursor.executescript(f.read())

# lê e executa insert_data.sql
with open("../sql/insert_data.sql", "r") as f:
    cursor.executescript(f.read())

# salva e fecha
conn.commit()
conn.close()

print("Banco criado e dados inseridos com sucesso.")