#importing packages we need
from flask import Flask, jsonify, request
from flask_cors import CORS

#creating the server and storing it in app and allowing JS and Python to talk with CORS
app = Flask(__name__)
CORS(app)

#create the books object
books = [
    { "title": "Inspired", "author": "Marty Cagan", "description": "The Agile and OKR playbook for developing tech products" },
    { "title": "The 21 Irrefutable Laws of Leadership", "author": "John Maxwell", "description": "The leadership playbook on how to lead teams and get better"    },
    { "title": "Good to Great", "author": "Jim Collins", "description": "What differentiates the truly great companies from just good"    }
]

#creating an HTTP GET method which retrieves a list of books
@app.route("/books", methods=["GET"])
def get_books():
    #function to return the books list as JSON
    return jsonify(books)

#creating an HTTP POST method which creates new books
@app.route("/books", methods=["POST"])
def add_book():
    #function to get the new book from the request and add it to the list
    new_book = request.json
    books.append(new_book)
    return jsonify(new_book), 201

#creating an HTTP DELETE method which deletes books
@app.route("/books/<int:index>", methods=["DELETE"])
def delete_book(index):
    #function to delete books
    books.pop(index)
    return jsonify({ "message": "deleted" }), 200

#creating an HTTP PUT method which edits books
@app.route("/books/<int:index>", methods=["PUT"])
def update_book(index):
    books[index] = request.json
    return jsonify(books[index]), 200


if __name__ == "__main__":
    app.run(debug=True)