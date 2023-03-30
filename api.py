from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# create some mock data for testing
books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'id': 3, 'title': '1984', 'author': 'George Orwell'}
]

# define endpoints for the API
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)
    return jsonify({'book': book[0]})

@app.route('/books', methods=['POST'])
def add_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json.get('author', '')
    }
    books.append(book)
    return jsonify({'book': book}), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)
    if not request.json:
        abort(400)
    book[0]['title'] = request.json.get('title', book[0]['title'])
    book[0]['author'] = request.json.get('author', book[0]['author'])
    return jsonify({'book': book[0]})

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)
    books.remove(book[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)