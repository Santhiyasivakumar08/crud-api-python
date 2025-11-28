README.md for my project
## Flask + MySQL CRUD API (Pure Python)

This is a simple CRUD (Create, Read, Update, Delete) REST API built using Python, Flask, and MySQL.  
It allows you to add, view, update, and delete items from a database through API endpoints.

This project was created as a task assignment for learning backend development.

---

## Features
- Create new items  
- Retrieve all items  
- Retrieve a single item by ID  
- Update existing items  
- Delete items  
- Uses MySQL database  
- Written in pure Python (without ORM)  

---

## Project Structure


project-folder/
│── app.py
│── README.md


---

## Technologies Used
- **Python 3**
- **Flask**
- **MySQL**
- **mysql-connector-python**
- **Postman for API testing**

---

## MySQL Database Setup

Run these queries in MySQL:

## sql
CREATE DATABASE crud_demo;
USE crud_demo;

CREATE TABLE items(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT
);

 Installation & Setup
1. Install required Python packages
pip install flask mysql-connector-python

2. Update your MySQL connection (inside app.py)
host="localhost",
user="root",
password="", 
database="crud_demo"

3. Run the Flask server
python app.py


## API will run at:

http://127.0.0.1:5000/

## API Endpoints
1. Create Item

POST /items

Body:

{
  "name": "Santhiya",
  "description": "good girl"
}

2. Get All Items

GET /items

3. Get Item by ID

GET /items/<id>

Example:
/items/1

4. Update Item

PUT /items/<id>

Body:

{
  "name": "Updated Name",
  "description": "Updated Description"
}

5. Delete Item

DELETE /items/<id>

Testing with Postman

Open Postman

Enter the API URL

Choose method: GET / POST / PUT / DELETE

For POST & PUT → Go to Body → raw → JSON

Send and check response

## Notes:

Make sure MySQL server is running

Ensure database name & credentials match

Use correct JSON format in POST/PUT

## About the Developer

This project was created by S. Santhiya while learning backend development using Python.
