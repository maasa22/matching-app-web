import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import send_from_directory
import pandas as pd
import config
import psycopg2
import json

user_db = config.user_db
password_db = config.password_db
host_db = config.host_db
port_db = config.port_db
database = config.database

# class User:
#     def __init__(self,id_user,gender,password,mail,birthday,display_name,self_images,self_introduction,favorites,last_login):
#         self.id_user = id_user
#         self.gender = gender
#         self.password = password
#         self.mail = mail
#         self.birthday = birthday
#         self.display_name = display_name
#         self.self_images = self_images
#         self.self_introduction = self_introduction
#         self.favorites = favorites
#         self.last_login = last_login


BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route("/static/<filename>")
def default_image(filename):
    return send_from_directory("./static", filename)

@app.route("/users_m", methods=['GET'])
def male_users():
    conn = psycopg2.connect("postgresql://{}:{}@{}:{}/{}".format(user_db, password_db, host_db, port_db, database))
    cur = conn.cursor()
    df = pd.read_sql("SELECT * FROM user_web WHERE gender = 'male'", con=conn)
    # users = []
    # for record in json.loads(df.to_json(orient="records")):
    #     users.append(User(**record))
    return df.to_json(orient="records")

@app.route('/user/<user_id>', methods=['GET'])
def single_user(user_id):
    response_object = {'status': 'success'}
    print(user_id)
    conn = psycopg2.connect("postgresql://{}:{}@{}:{}/{}".format(user_db, password_db, host_db, port_db, database))
    cur = conn.cursor()
    df = pd.read_sql("SELECT * FROM user_web WHERE id_user = '{}'".format(user_id),  con=conn)
    return df.to_json(orient="records")

@app.route('/user_by_conditions', methods=['GET', 'POST'])
def user_by_conditions():
    response_object = {'status': 'success'}
    age_min = request.args.get('age_min')
    age_max = request.args.get('age_max')
    prefectures = request.args.getlist('prefecture[]')
    conn = psycopg2.connect("postgresql://{}:{}@{}:{}/{}".format(user_db, password_db, host_db, port_db, database))
    cur = conn.cursor()
    if len(prefectures) >= 1:
        prefectures_str = "("
        for i in range(len(prefectures)):
            prefectures_str += "'" + prefectures[i] + "', "
            if i == len(prefectures) - 1:
                prefectures_str += "'" + prefectures[i] + "')"
        df = pd.read_sql("SELECT * FROM user_web WHERE age > '{}' and age < '{}' and prefecture in {}".format(age_min, age_max, prefectures_str),  con=conn)
    else:
        df = pd.read_sql("SELECT * FROM user_web WHERE age > '{}' and age < '{}'".format(age_min, age_max),  con=conn)
    return df.to_json(orient="records")

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
