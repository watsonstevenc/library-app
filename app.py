#importing packages we need
import os
import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()


#creating the server and storing it in app and allowing JS and Python to talk with CORS
app = Flask(__name__)
CORS(app)

#create database
def get_db():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title TEXT,
            author TEXT,
            description TEXT
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

init_db()




#creating an HTTP GET method which retrieves a list of books
@app.route("/books", methods=["GET"])
def get_books():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, title, author, description FROM books")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": r[0], "title": r[1], "author": r[2], "description": r[3]} for r in rows])

#creating an HTTP POST method which creates new books
@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author, description) VALUES (%s, %s, %s)", 
                (data["title"], data["author"], data["description"]))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(data), 201

#creating an HTTP DELETE method which deletes books
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "deleted"}), 200

#creating an HTTP PUT method which edits books
@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    data = request.json
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=%s, author=%s, description=%s WHERE id=%s",
                (data["title"], data["author"], data["description"], id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(data), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
