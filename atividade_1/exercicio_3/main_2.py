from db.db_utils import *

# Cria a tabela
criar_tabela('Estudantes', 'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, curso TEXT NOT NULL, ano_ingresso INTEGER NOT NULL')

# Insere dados na tabela
print('Inserindo dados na tabela Estudantes: \n')
print('Inserção 1:')
inserir_dados('Estudantes', 'nome, curso, ano_ingresso', "'Ana Silva', 'Computação', 2019")

print('\nInserção 2:')
inserir_dados('Estudantes', 'nome, curso, ano_ingresso', "'Pedro Mendes', 'Física', 2021")

print('\nInserção 3:')
inserir_dados('Estudantes', 'nome, curso, ano_ingresso', "'Carla Souza', 'Computação', 2020")

print('\nInserção 4:')
inserir_dados('Estudantes', 'nome, curso, ano_ingresso', "'João Alves', 'Matemática', 2018")

print('\nInserção 5:')
inserir_dados('Estudantes', 'nome, curso, ano_ingresso', "'Maria Oliveira', 'Química', 2022")

print('\n')
print('\n')

# Atualiza os dados da tabela

print('Estudantes que ingressaram em 2019 ou 2020:\n')
selecionar_dados('Estudantes', '*', 'ano_ingresso = 2020 or ano_ingresso = 2019')

print('\n')

# Atualiza o ano de ingresso de um estudante

print('Atualizando o ano de ingresso do estudante de id = 1 para 2021\n')

selecionar_dados('Estudantes', '*', 'id = 1')
atualizar_dados('Estudantes', 'ano_ingresso', 2021, 'id = 1')
selecionar_dados('Estudantes', '*', 'id = 1')

# Deleta um estudante a partir do id

print('\nDeletando o estudante de id = 2\n')
selecionar_todos_dados('Estudantes')
deletar_dados('Estudantes', 'id = 2')

print('\nTodos os estudantes depois da deleção:\n')
selecionar_todos_dados('Estudantes')