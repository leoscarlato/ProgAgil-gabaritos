import sqlite3

# Cria uma conexão com o banco de dados
conn = sqlite3.connect('atividade_1/db/atividade_1.db')

# Cria um cursor para manipular o banco de dados
cursor = conn.cursor()

# Cria a tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        curso TEXT NOT NULL,
        ano_ingresso INTEGER NOT NULL)
""")

# Insere dados na tabela
cursor.execute("""
INSERT INTO Estudantes (nome, curso, ano_ingresso)
VALUES ('Ana Silva', 'Computação', 2019),
        ('Pedro Mendes', 'Física', 2021),
        ('Carla Souza', 'Computação', 2020),
        ('João Alves', 'Matemática', 2018),
        ('Maria Oliveira', 'Química', 2022)
""")
conn.commit()

# Atualiza os dados da tabela
cursor.execute(""" SELECT * FROM Estudantes WHERE ano_ingresso = 2020 or ano_ingresso = 2019 """)

print('Estudantes que ingressaram em 2019 ou 2020:')
for linha in cursor.fetchall():
        print(linha)

print("\n")

# Atualiza o ano de ingresso de um estudante

print('Atualizando o ano de ingresso do estudante de id = 1 para 2021')

cursor.execute(""" SELECT * FROM Estudantes WHERE id = 1 """)
print('Dados do estudante antes da atualização:')
for linha in cursor.fetchall():
        print(linha)

cursor.execute("""
UPDATE Estudantes
SET ano_ingresso = 2021
WHERE id = 1
""")
conn.commit()

cursor.execute(""" SELECT * FROM Estudantes WHERE id = 1 """)
print('Dados do estudante depois da atualização:')
for linha in cursor.fetchall():
        print(linha)

print("\n")

# Deleta um estudante a partir do id

print('Deletando o estudante de id = 2')

cursor.execute(""" SELECT * FROM Estudantes""")
print('Todos os estudantes antes da deleção:')
for linha in cursor.fetchall():
        print(linha)

cursor.execute("""
DELETE FROM Estudantes
WHERE id = 2
""")

conn.commit()

cursor.execute(""" SELECT * FROM Estudantes""")
print('Todos os estudantes depois da deleção:')
for linha in cursor.fetchall():
        print(linha)

print("\n")

# Filtra e mostra os estudantes de Ciência da Computação que ingressaram após 2019

print('Estudantes de Ciência da Computação que ingressaram após 2019:')
cursor.execute(""" SELECT * FROM Estudantes WHERE curso = 'Computação' and ano_ingresso > 2019 """)
for linha in cursor.fetchall():
        print(linha)

print("\n")

# Imagine que alguém errou nos registros de ingresso de todos os alunos do curso de Computação, crie uma query que altere todos os registros dos alunos de Computação, campo ingresso para 2018. Mostre por todos estudantes novamente.

print('Atualizando o ano de ingresso de todos os estudantes de Computação para 2018')

cursor.execute(""" SELECT * FROM Estudantes WHERE curso = 'Computação' """)
print('Todos os estudantes de Computação antes da atualização:')
for linha in cursor.fetchall():
        print(linha)

cursor.execute("""
UPDATE Estudantes
SET ano_ingresso = 2018
WHERE curso = 'Computação'
""")

conn.commit()

cursor.execute(""" SELECT * FROM Estudantes WHERE curso = 'Computação' """)
print('Todos os estudantes de Computação depois da atualização:')
for linha in cursor.fetchall():
        print(linha)


