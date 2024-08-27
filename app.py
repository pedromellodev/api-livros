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
@app.route('/livros')
def obter_livros():
    return jsonify(livros)

# Consultar(id)
# Editar
# Excluir

app.run(port=5000, host='localhost', debug=True)