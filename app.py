from bson import ObjectId
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://awab:awab@cluster0.iagtyub.mongodb.net/")
db = client.test


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create-user')
def add_user():
    return render_template('adduser.html')


@app.route('/update-user')
def update_user():
    users = db.users.find()
    return render_template('updateuser.html', users=users)


@app.route('/delete-user')
def delete_user_page():
    users = db.users.find()
    return render_template('deleteuser.html', users=users)


@app.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = request.form['name']
    db.users.delete_one({'_id': ObjectId(user_id)})
    return 'Thanks for deleting!'


@app.route('/update_user', methods=['POST'])
def update_user_post():
    user_id = request.form['name']
    email = request.form['email']
    password = request.form['password']

    db.users.update_one({'_id': ObjectId(user_id)},
                        {'$set': {
                            'email': email,
                            'password': password
                        }})
    return 'Thanks for updating!'


@app.route('/create_user', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    db.users.insert_one({
        'name': name,
        'email': email,
        'password': password
    })
    return f'Thanks for creating {name}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
