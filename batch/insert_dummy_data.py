import uuid
import config
import psycopg2
import datetime

user = config.user
password = config.password
host = config.host
port_db = config.port_db
database = config.database

conn = psycopg2.connect("postgresql://{}:{}@{}:{}/{}".format(user, password, host, port_db, database))
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS user_web")
cur.execute('''CREATE TABLE user_web \
                (id_user text, \
                gender text,
                password text,\
                mail text, \
                birthday date, \
                display_name text, \
                self_images text, \
                self_introduction text, \
                favorites numeric, \
                last_login timestamp \
                )''')

cur.execute("INSERT INTO user_web VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}')".format( \
    uuid.uuid4().hex,\
    'male', \
    'hoge',\
    'hoge@hoge',\
    datetime.date(1994, 11, 18),\
    'hoge',\
    'http://localhost:5000/static/image/test.png',\
    'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry''s standard dummy text ever since the 1500s...',\
    48,\
    datetime.datetime(2010, 2, 8, 1, 40, 27, 425337)\
))
cur.execute("INSERT INTO user_web VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}')".format( \
    uuid.uuid4().hex,\
    'male', \
    'fuga',\
    'fuga@fuga',\
    datetime.date(1994, 11, 17),\
    'fuga',\
    'http://localhost:5000/static/image/test.png',\
    'この文章はダミーです。文字の大きさ、量、字間、行間等を確認するために入れています。',\
    46,\
    datetime.datetime.now()\
))

cur.execute("INSERT INTO user_web VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}')".format( \
    uuid.uuid4().hex,\
    'female', \
    'fuga',\
    'fuga@fuga',\
    datetime.date(1994, 11, 17),\
    'fuga',\
    'http://localhost:5000/static/image/test.png',\
    'この文章はダミーです。文字の大きさ、量、字間、行間等を確認するために入れています。',\
    46,\
    datetime.datetime.now()\
))

cur.execute("INSERT INTO user_web VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}')".format( \
    uuid.uuid4().hex,\
    'female', \
    'fuga',\
    'fuga@fuga',\
    datetime.date(1994, 11, 17),\
    'fuga',\
    'http://localhost:5000/static/image/test.png',\
    'この文章はダミーです。文字の大きさ、量、字間、行間等を確認するために入れています。',\
    46,\
    datetime.datetime.now()\
))


conn.commit()
conn.close()
