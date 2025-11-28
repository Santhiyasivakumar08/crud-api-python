#Step1-CREATE DATABASE crud_demo;

# USE crud_demo;
# CREATE TABLE items(
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     description TEXT
# );

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Connection
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # your MySQL username
        password="",  # your MySQL password
        database="crud_demo"
    )

# CREATE
@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    name = data["name"]
    desc = data.get("description", "")

    db = get_db()
    cursor = db.cursor()

    cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (name, desc))
    db.commit()

    new_id = cursor.lastrowid

    cursor.close()
    db.close()

    return jsonify({"id": new_id, "name": name, "description": desc}), 201


# READ ALL
@app.route("/items", methods=["GET"])
def get_items():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(rows), 200


# READ ONE 
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
    row = cursor.fetchone()

    cursor.close()
    db.close()

    if row:
        return jsonify(row)
    return jsonify({"error": "Item not found"}), 404


# UPDATE 
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    name = data.get("name")
    desc = data.get("description")

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "UPDATE items SET name = %s, description = %s WHERE id = %s",
        (name, desc, item_id),
    )
    db.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "Item not found"}), 404

    cursor.close()
    db.close()

    return jsonify({"message": "Item updated"}), 200


# DELETE 
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
    db.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "Item not found"}), 404

    cursor.close()
    db.close()

    return jsonify({"message": "Item deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
