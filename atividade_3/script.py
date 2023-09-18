import sqlite3

conn = sqlite3.connect('atividade_3/db/atividade_3.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_publicacao INTEGER NOT NULL,
    genero TEXT NOT NULL
               )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    data_nascimento DATE NOT NULL
                )
""")