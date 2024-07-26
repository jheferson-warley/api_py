from flask import Flask, jsonify,request

app =  Flask(__name__)

books = [
  {
    'id': 1,
    'título':  'Campo de batalha da mente, de Joyce Meyer',
    'autor': 'Joyce Meyer'
  },
  {
    'id': 2,
    'título':  'Um ano com C.S. Lewis',
    'autor': 'C.S Lewis'
  },
  {
    'id': 3,
    'título':  'O Evangelho maltrapilho',
    'autor': 'Brennan Manning'
  },
  {
    'id': 4,
    'título':  'Hábitos Atômicos',
    'autor': 'James Clear'
  }
]

#Consultar(todos)
@app.route('/books', methods=['GET'])
def obter_books():
  return jsonify(books)
#Consultar(id)
@app.route('/books/<int:id>',  methods=['GET'])
def obter_book_por_id(id):
  for book in books:
    if book.get('id') == id:
      return jsonify(book)
#Editar
@app.route('/books/<int:id>',  methods=['PUT'])
def edit_book_por_id(id):
  book_alterado = request.get_json()
  for indice, book in enumerate(books):
    if book.get('id') == id: 
      books[indice].update(book_alterado)
      return jsonify(books[indice])
    
#Criar
@app.route('/books', methods=['POST'])
def incluir_new_book():
  new_book = request.get_json()
  books.append(new_book)

  return jsonify(books)
#Excluir
@app.route('/books/<int:id>',  methods=['DELETE'])
def excluir_book(id):
    for indice, book in enumerate(books):
      if book.get('id') == id:
        del books[indice]
        return jsonify(books)
app.run(port=5000, host='localhost', debug=True)