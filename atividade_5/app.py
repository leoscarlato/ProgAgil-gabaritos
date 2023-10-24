import datetime
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId
from credentials_file import settings, credenciais

app = Flask(__name__)
app.config["MONGO_URI"] = f"mongodb+srv://{credenciais['user']}:{credenciais['password']}@{settings['host']}/{settings['database']}?retryWrites=true&w=majority"
mongo = PyMongo(app)

# rota de teste de funcionamento da API
@app.route('/')
def index():
    return {"mensagem": "Api em funcionamento"}, 200

# Cadastro de usuarios
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    try:
        data = request.json
        if not all(k in data for k in ("nome", "cpf", "data de nascimento")):
            return jsonify({"erro": "Campos obrigatórios faltando!"}), 400
        
        # verificamos se existe um usuário com o mesmo cpf, e se sim, retornamos um erro
        usuario = mongo.db.usuarios.find_one({"cpf": data["cpf"]})
        if usuario:
            return {"erro": "Já existe um usuário com este CPF"}, 400

        usuario_id = mongo.db.usuarios.insert_one(data)
        print(usuario_id.inserted_id)
        return {"_id": str(usuario_id.inserted_id)}, 201
    except Exception as e:
        return {"erro":str(e)}, 500


# leitura de usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    try:
        filter_ = {}
        projection_ = {}
        usuarios = list(mongo.db.usuarios.find(filter_, projection_))
        for usuario in usuarios:
            usuario["_id"] = str(usuario["_id"])
        return {"usuários": usuarios}, 200
    except Exception as e:
        return {"erro":str(e)}, 500
    
# leitura de usuarios por id
@app.route('/usuarios/<id>', methods=['GET'])
def get_usuario(id):
    try:
        usuario = mongo.db.usuarios.find_one({"_id": ObjectId(id)})
        if usuario:
            usuario["_id"] = str(usuario["_id"])
            return {"usuário": usuario}, 200
        else:
            return {"erro": "Usuário não encontrado"}, 404
    except Exception as e:
        return {"erro":str(e)}, 500
    
# alterar um usuario por id
@app.route('/usuarios/<id>', methods=['PUT'])
def update_usuario(id):
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Dado para atualização não fornecido!"}), 400

        usuario = mongo.db.usuarios.find_one({"_id": ObjectId(id)})
        if usuario:
            mongo.db.usuarios.update_one({"_id": ObjectId(id)}, {"$set": data})
            return {"mensagem": f"Usuário {id} alterado com sucesso"}, 200
        else:
            return {"erro": "Usuário não encontrado"}, 404
    except Exception as e:
        return {"erro":str(e)}, 500
    
# deletar um usuario por id
@app.route('/usuarios/<id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        usuario = mongo.db.usuarios.find_one({"_id": ObjectId(id)})
        if usuario:
            mongo.db.usuarios.delete_one({"_id": ObjectId(id)})
            return {"mensagem": f"Usuário {id} removido com sucesso"}, 200
        else:
            return {"erro": "Usuário não encontrado"}, 404
    except Exception as e:
        return {"erro":str(e)}, 500
    
# Cadastro de bicicletas
@app.route('/bikes', methods=['POST'])
def create_bike():
    try:
        data = request.json
        if not all(k in data for k in ("marca", "modelo", "cidade")):
            return jsonify({"erro": "Campos obrigatórios faltando!"}), 400

        data["status"] = "disponível"
        bike_id = mongo.db.bikes.insert_one(data)
        print(bike_id.inserted_id)
        return {"_id": str(bike_id.inserted_id)}, 201
    except Exception as e:
        return {"erro":str(e)}, 500
    
# leitura de bicicletas
@app.route('/bikes', methods=['GET'])
def get_bikes():
    try:
        filter_ = {}
        projection_ = {}
        bikes = list(mongo.db.bikes.find(filter_, projection_))
        for bike in bikes:
            bike["_id"] = str(bike["_id"])
        return {"bicicletas": bikes}, 200
    except Exception as e:
        return {"erro":str(e)}, 500

# leitura de bicicletas por id
@app.route('/bikes/<id>', methods=['GET'])
def get_bike(id):
    try:
        bike = mongo.db.bikes.find_one({"_id": ObjectId(id)})
        if bike:
            bike["_id"] = str(bike["_id"])
            return {"bicicleta": bike}, 200
        else:
            return {"erro": "Bicicleta não encontrada"}, 404
    except Exception as e:
        return {"erro":str(e)}, 500
    
# alterar uma bicicleta por id
@app.route('/bikes/<id>', methods=['PUT'])
def update_bike(id):
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Dado para atualização não fornecido!"}), 400

        bike = mongo.db.bikes.find_one({"_id": ObjectId(id)})
        if bike:
            mongo.db.bikes.update_one({"_id": ObjectId(id)}, {"$set": data})
            return {"mensagem": f"Bicicleta {id} alterada com sucesso"}, 200
        else:
            return {"erro": "Bicicleta não encontrada"}, 404
    except Exception as e:
        return {"erro":str(e)}, 500

# deletar uma bicicleta por id
@app.route('/bikes/<id>', methods=['DELETE'])
def delete_bike(id):
    try:
        bike = mongo.db.bikes.find_one({"_id": ObjectId(id)})
        if bike:
            mongo.db.bikes.delete_one({"_id": ObjectId(id)})
            return {"mensagem": f"Bicicleta {id} removida com sucesso"}, 200
        else:
            return {"erro": "Bicicleta não encontrada"}, 404
    except Exception as e:
        return {"erro":str(e)}, 500
    
# criar um emprestimo por id de usuario e id de bicicleta
@app.route('/emprestimos/usuarios/<id_usuario>/bikes/<id_bike>', methods=['POST'])
def create_emprestimo(id_usuario, id_bike):
    try:
        usuario = mongo.db.usuarios.find_one({"_id": ObjectId(id_usuario)})
        bike = mongo.db.bikes.find_one({"_id": ObjectId(id_bike)})
        if not usuario:
            return {"erro": "Usuário não encontrado"}, 404
        if not bike:
            return {"erro": "Bicicleta não encontrada"}, 404
        if bike["status"] != "disponível":
            return {"erro": "Bicicleta indisponível"}, 400

        # atualizamos o status da bike para "em uso"
        data_bike = {"status": "em uso"}
        mongo.db.bikes.update_one({"_id": ObjectId(id_bike)}, {"$set": data_bike})

        # usamos a biblioteca datetime para obter a data e hora atual
        current_datetime = datetime.datetime.now()
        data = {"usuario": usuario["_id"], "bike": bike["_id"], "data_emprestimo": str(current_datetime.day) + "/" + str(current_datetime.month) + "/" + str(current_datetime.year)}
        emprestimo_id = mongo.db.emprestimos.insert_one(data)
        return {"_id": str(emprestimo_id.inserted_id)}, 201
    except Exception as e:
        return {"erro":str(e)}, 500
    
# leitura de emprestimos mostrando o id do usuario, da bicicleta e do emprestimo
@app.route('/emprestimos', methods=['GET'])
def get_emprestimos():
    try:
        filter_ = {}
        projection_ = {}
        emprestimos = list(mongo.db.emprestimos.find(filter_, projection_))
        for emprestimo in emprestimos:
            emprestimo["_id"] = str(emprestimo["_id"])
            emprestimo["usuario"] = str(emprestimo["usuario"])
            emprestimo["bike"] = str(emprestimo["bike"])
        return {"emprestimos": emprestimos}, 200
    except Exception as e:
        return {"erro":str(e)}, 500

# deletar um emprestimo por id
@app.route('/emprestimos/<id>', methods=['DELETE'])
def delete_emprestimo(id):
    try:
        emprestimo = mongo.db.emprestimos.find_one({"_id": ObjectId(id)})

        # lembrar de atualizar o status da bike para "disponível"
        data_bike = {"status": "disponível"}
        mongo.db.bikes.update_one({"_id": ObjectId(emprestimo["bike"])}, {"$set": data_bike})

        if emprestimo:
            mongo.db.emprestimos.delete_one({"_id": ObjectId(id)})
            return {"mensagem": f"Empréstimo {id} removido com sucesso"}, 200
        else:
            return {"erro": "Empréstimo não encontrado"}, 404
    except Exception as e:
        return {"erro":str(e)}, 500