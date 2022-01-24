from flask import Flask, request, jsonify
from model import servicos, integrantes, blogs, visualizacoes
from data import alchemy
from flask_cors import CORS

#cria a aplicação flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'cronos'
CORS(app)

@app.before_first_request
def create_tables():
    alchemy.create_all()

@app.route('/', methods=['GET'])
def home():
    return {'message': 'Api funcionado'}, 200

# region Servicos
@app.route('/servicos/',  methods=['POST'])
def create_servico():
    "Cria um serviço"
    request_data = request.get_json()
    new_servicos = servicos.Servico(request_data['nome'],
                                      request_data['caminho_imagem'],
                                      request_data['descricao']
                                      )

    new_servicos.save_to_db()
    result = new_servicos.find_by_id(new_servicos.id)
    return jsonify(result.json())

@app.route('/servicos/', methods=['GET'])
def get_all_servico():
    "Retorna todos os servicos"
    result = servicos.Servico.query.all()
    items = []
    for item in result:
        items.append(item.json())
    if items:
        return jsonify(items)
    else:
        return {'message': 'Serviços não encontrados'}, 404

@app.route('/servicos/<int:id>/')
def get_servico(id):
    "Retorna o servico especifico por id"
    result = servicos.Servico.find_by_id(id)
    if result:
        return result.json()
    else:
        return {'message': 'Serviço não encontrado'}, 404

@app.route('/servicos/<int:id>/', methods=['DELETE'])
def delete_servico(id):
    servico_deleted = servicos.Servico.find_by_id(id)
    servico_deleted.delete_from_db()
    return {'message':'Serviço excluído com sucesso'}, 202

@app.route('/servicos/<int:id>/', methods=['PUT'])
def update_servico(id):
    request_data = request.get_json()
    servico_updated = servicos.Servico.find_by_id(id)
    servico_updated.id = id
    servico_updated.nome = request_data['nome']
    servico_updated.caminho_imagem = request_data['caminho_imagem']
    servico_updated.descricao = request_data['descricao']
    servico_updated.save_to_db()
    result = servico_updated.find_by_id(id)
    if result:
        return result.json(), 200
    else:
        return {'message': 'Serviços não encontrados'}, 404
#endregion

# region Integrantes
@app.route('/integrantes/',  methods=['POST'])
def create_integrante():
    "Cria um serviço"
    request_data = request.get_json()
    new_membros = integrantes.Integrante(request_data['nome'],
                                      request_data['email'],
                                      request_data['departamento']
                                      )

    new_membros.save_to_db()
    result = new_membros.find_by_id(new_membros.id)
    return jsonify(result.json())

@app.route('/integrantes/', methods=['GET'])
def get_all_integrante():
    "Retorna todos os integrantes"
    result = integrantes.Integrante.query.all()
    items = []
    for item in result:
        items.append(item.json())
    if items:
        return jsonify(items)
    else:
        return {'message': 'Integrantes não encontrados'}, 404

@app.route('/integrantes/<int:id>/')
def get_membro(id):
    "Retorna o membro especifico por id"
    result = integrantes.Integrante.find_by_id(id)
    if result:
        return result.json()
    else:
        return {'message': 'Membro não encontrado'}, 404

@app.route('/integrantes/<int:id>/', methods=['DELETE'])
def delete_membro(id):
    membro_deleted = integrantes.Integrante.find_by_id(id)
    membro_deleted.delete_from_db()
    return {'message':'Membro excluído com sucesso'}, 202


@app.route('/integrantes/<int:id>/', methods=['PUT'])
def update_membro(id):
    request_data = request.get_json()
    membro_updated = integrantes.Integrante.find_by_id(id)
    membro_updated.id = id
    membro_updated.nome = request_data['nome']
    membro_updated.email = request_data['email']
    membro_updated.departamento = request_data['departamento']
    result = membro_updated.find_by_id(id)
    if result:
        return result.json(), 200
    else:
        return {'message': 'Membro não encontrados'}, 404

# endregion

# region Blogs
@app.route('/blogs/',  methods=['POST'])
def create_Blog():
    "Cria um blog"
    request_data = request.get_json()
    new_blogs = blogs.Blog(request_data['titulo'],
                           request_data['conteudo']
                          )

    new_blogs.save_to_db()
    result = new_blogs.find_by_id(new_blogs.id)
    return jsonify(result.json())

@app.route('/blogs/', methods=['GET'])
def get_all_Blog():
    "Retorna todos os blogs"
    result = blogs.Blog.query.all()
    items = []
    for item in result:
        items.append(item.json())
    if items:
        return jsonify(items)
    else:
        return {'message': 'Blogs não encontrados'}, 404

@app.route('/blogs/<int:id>/')
def get_Blog(id):
    "Retorna o Blog especifico por id"
    result = blogs.Blog.find_by_id(id)
    if result:
        return result.json()
    else:
        return {'message': 'Blog não encontrado'}, 404

@app.route('/blogs/<int:id>/', methods=['DELETE'])
def delete_Blog(id):
    "Deleta o blog por id"
    Blog_deleted = blogs.Blog.find_by_id(id)
    Blog_deleted.delete_from_db()
    return {'message':'Blog excluído com sucesso'}, 202


@app.route('/blogs/<int:id>/', methods=['PUT'])
def update_Blog(id):
    "Realiza o update do blog"
    request_data = request.get_json()
    Blog_updated = blogs.Blog.find_by_id(id)
    Blog_updated.id = id
    Blog_updated.titulo = request_data['titulo']
    Blog_updated.conteudo = request_data['conteudo']
    result = Blog_updated.find_by_id(id)
    if result:
        return result.json(), 200
    else:
        return {'message': 'Blog não encontrados'}, 404

# endregion

# region Visulizacoes
@app.route('/visualizacoes/',  methods=['POST'])
def create_visualizacao():
    "Cria um serviço"
    request_data = request.get_json()
    new_visualizacoes = visualizacoes.Visualizacao(request_data['titulo'],
                           request_data['conteudo']
                          )

    new_visualizacoes.save_to_db()
    result = new_visualizacoes.find_by_id(new_visualizacoes.id)
    return jsonify(result.json())

@app.route('/visualizacoes/', methods=['GET'])
def get_all_visualizacoes():
    "Retorna todas as visualizacoes"
    result = visualizacoes.Visualizacao.query.all()
    items = []
    for item in result:
        items.append(item.json())
    if items:
        return jsonify(items)
    else:
        return {'message': 'Visualizações não encontradas'}, 404

@app.route('/visualizacoes/<int:id>/')
def get_visualizacao(id):
    "Retorna a visualizacao especifica por id"
    result = visualizacoes.Visualizacao.find_by_id(id)
    if result:
        return result.json()
    else:
        return {'message': 'Visualizacao não encontrada'}, 404


@app.route('/visualizacoes/<int:id>/', methods=['PUT'])
def update_visualizacao():
    "Realiza o update da visualizacao"
    request_data = request.get_json()
    Blog_updated = visualizacoes.Visualizacao.find_by_id(id)
    Blog_updated.id = id
    Blog_updated.visulizacoes = Blog_updated.visulizacoes + 1
    result = Blog_updated.find_by_id(id)
    if result:
        return result.json(), 200
    else:
        return {'message': 'Visualizacao não encontrada'}, 404

# endregion

#Parametros de inicialização da API
if __name__ == '__main__':
    from data import alchemy
    alchemy.init_app(app)
    app.run(port=8000, debug=True)