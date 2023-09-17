from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "atividade_2/db/atividade_2.db"

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/livro', methods=['POST'])
def create_livro():
    conn = sqlite3.connect(DATABASE)

    data = request.get_json()

    titulo = data['titulo']
    autor = data['autor']
    ano_publicacao = data['ano_publicacao']
    genero = data['genero']

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO livros (titulo, autor, ano_publicacao, genero)
    VALUES (?, ?, ?, ?)
    """, (titulo, autor, ano_publicacao, genero))

    conn.commit()

    return {'mensagem': 'Livro criado com sucesso!'}, 201

@app.route('/livro', methods=['GET'])
def get_livros():
    conn = sqlite3.connect(DATABASE)

    genero = request.args.get('genero')

    cursor = conn.cursor()

    if genero:
        cursor.execute("""
        SELECT * FROM livros WHERE genero = ?;
        """, (genero,))
    else:
        cursor.execute("""
        SELECT * FROM livros;
        """)

    livros = cursor.fetchall()

    return jsonify(livros), 200

@app.route('/livro/<int:id>', methods=['GET'])
def get_livro_by_id(id):
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM livros WHERE id = ?;
    """, (id,))

    # verificar se o livro existe
    livro = cursor.fetchone()

    if not livro:
        return {'mensagem': 'Livro não encontrado!'}, 404
    
    return jsonify(livro), 200

@app.route('/livro/<int:id>', methods=['PUT'])
def update_livro(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    data = request.get_json()

    for key in data.keys():
        if key not in ['titulo', 'autor', 'ano_publicacao', 'genero']:
            return {'mensagem': f'Chave {key} inválida!'}, 400
        
    # verificar se o livro existe
    cursor.execute("""
    SELECT * FROM livros WHERE id = ?;
    """, (id,))
    livro = cursor.fetchone()

    if not livro:
        return {'mensagem': 'Livro não encontrado!'}, 404
    
    for key, value in data.items():
        cursor.execute(f"""
        UPDATE livros SET {key} = ? WHERE id = ?;
        """, (value, id))

    conn.commit()

    return {'mensagem': 'Livro atualizado com sucesso!'}, 200

@app.route('/livro/<int:id>', methods=['DELETE'])
def delete_livro(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # verificar se o livro existe
    cursor.execute("""
    SELECT * FROM livros WHERE id = ?;
    """, (id,))
    livro = cursor.fetchone()

    if not livro:
        return {'mensagem': 'Livro não encontrado!'}, 404

    cursor.execute("""
    DELETE FROM livros WHERE id = ?;
    """, (id,))

    conn.commit()

    return {'mensagem': 'Livro deletado com sucesso!'}, 200

@app.route('/usuario', methods=['POST'])
def create_usuario():
    conn = sqlite3.connect(DATABASE)

    data = request.get_json()

    nome = data['nome']
    email = data['email']
    data_nascimento = data['data_nascimento']

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO usuarios (nome, email, data_nascimento)
    VALUES (?, ?, ?)
    """, (nome, email, data_nascimento))

    conn.commit()

    return {'mensagem': 'Usuário criado com sucesso!'}, 201

@app.route('/usuario', methods=['GET'])
def get_usuarios():
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM usuarios;
    """)

    usuarios = cursor.fetchall()

    return usuarios, 200

@app.route('/usuario/<int:id>', methods=['GET'])
def get_usuario_by_id(id):
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM usuarios WHERE id = ?;
    """, (id,))

    usuario = cursor.fetchone()

    if not usuario:
        return {'mensagem': 'Usuário não encontrado!'}, 404

    return jsonify(usuario), 200

@app.route('/usuario/<int:id>', methods=['PUT'])
def update_usuario(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    data = request.get_json()

    for key in data.keys():
        if key not in ['nome', 'email', 'data_nascimento']:
            return {'mensagem': f'Chave {key} inválida!'}, 400
        
    # verificar se o usuário existe
    cursor.execute("""
    SELECT * FROM usuarios WHERE id = ?;
    """, (id,))
    usuario = cursor.fetchone()

    if not usuario:
        return {'mensagem': 'Usuário não encontrado!'}, 404
        
    for key, value in data.items():
        cursor.execute(f"""
        UPDATE usuarios SET {key} = ? WHERE id = ?;
        """, (value, id))


    conn.commit()

    return {'mensagem': 'Usuário atualizado com sucesso!'}, 200

@app.route('/usuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # verificar se o usuário existe
    cursor.execute("""
    SELECT * FROM usuarios WHERE id = ?;
    """, (id,))
    usuario = cursor.fetchone()

    if not usuario:
        return {'mensagem': 'Usuário não encontrado!'}, 404
    

    cursor.execute("""
    DELETE FROM usuarios WHERE id = ?;
    """, (id,))

    conn.commit()

    return {'mensagem': 'Usuário deletado com sucesso!'}, 200


if __name__ == '__main__':
    app.run(debug=True)
    
