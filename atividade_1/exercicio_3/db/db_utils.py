import sqlite3

conn = sqlite3.connect('atividade_1/exercicio_3/db/ex3.db')

def criar_tabela(nome_tabela, colunas):
    cursor = conn.cursor()
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {nome_tabela} (
            {colunas}
    )
    """)
    conn.commit()

    # printar tabela
    cursor.execute(f"""
    SELECT * FROM {nome_tabela}
    """)
    for linha in cursor.fetchall():
        print(linha)

    conn.close()

def inserir_dados(nome_tabela, colunas, valores):
    conn = sqlite3.connect('atividade_1/exercicio_3/db/ex3.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    INSERT INTO {nome_tabela} ({colunas})
    VALUES ({valores})
    """)
    conn.commit()

    # printar tabela
    cursor.execute(f"""
    SELECT * FROM {nome_tabela}
    """)
    for linha in cursor.fetchall():
        print(linha)

    conn.close()

def atualizar_dados(nome_tabela, coluna, valor, condicao):
    conn = sqlite3.connect('atividade_1/exercicio_3/db/ex3.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    UPDATE {nome_tabela}
    SET {coluna} = {valor}
    WHERE {condicao}
    """)
    conn.commit()
    conn.close()

def selecionar_dados(nome_tabela, colunas, condicao):
    conn = sqlite3.connect('atividade_1/exercicio_3/db/ex3.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    SELECT {colunas} FROM {nome_tabela} WHERE {condicao}
    """)
    conn.commit()
    
    # printar tabela
    for linha in cursor.fetchall():
        print(linha)

    conn.close()

def deletar_dados(nome_tabela, condicao):
    conn = sqlite3.connect('atividade_1/exercicio_3/db/ex3.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    DELETE FROM {nome_tabela} WHERE {condicao}
    """)
    conn.commit()
    conn.close()

def selecionar_todos_dados(nome_tabela):
    conn = sqlite3.connect('atividade_1/exercicio_3/db/ex3.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    SELECT * FROM {nome_tabela}
    """)
    conn.commit()
    
    # printar tabela
    for linha in cursor.fetchall():
        print(linha)

    conn.close()