from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Coraline e o Mundo Secreto',
        'autor': 'Henry Sellick'
    },
    {
        'id': 2,
        'titulo': 'Naruto(Mangá)',
        'autor': 'Masashi Kishimoto'
    },
        {
        'id': 3,
        'titulo': 'Dragon Ball(Mangá)',
        'autor': 'Akira Toriyama'
    }
]

# Consultar(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def consultar_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar
@app.route('livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()

    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
# Excluir

app.run(port=5000, host='localhost', debug=True)