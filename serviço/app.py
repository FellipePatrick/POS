import json
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({
        "nome": "Alice",
        "email": "alice@outlook.com",
    })



@app.route('/user/<int:user_id>')
def users(user_id):
   if(user_id == 1):
        return jsonify ({"nome": "Alice","email": "alice@outlook.com","id": "1"})
   elif(user_id == 2):
         return jsonify ({"nome": "Fernando","email": "fernando@outlook.com","id": "2"})

   
app.run()