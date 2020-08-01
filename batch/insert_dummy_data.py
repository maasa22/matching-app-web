import uuid
import config
import psycopg2
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

user = config.user
password = config.password
host = config.host
port_db = config.port_db
database = config.database

conn = psycopg2.connect("postgresql://{}:{}@{}:{}/{}".format(user, password, host, port_db, database))
cur = conn.cursor()

# batch udpates: age, favorites, last_login
# realtime updates: display_name, self_images, self_introduction, prefecture
cur.execute("DROP TABLE IF EXISTS user_web")
cur.execute('''CREATE TABLE user_web \
                (id_user text, \
                gender text,
                password text,\
                mail text, \
                birthday date, \
                prefecture text, \
                display_name text, \
                self_status_message text,
                self_images text, \
                self_introduction text, \
                age numeric, \
                favorites numeric, \
                last_login timestamp \
                )''')

cur.execute("INSERT INTO user_web VALUES ('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}')".format( \
    uuid.uuid4().hex,\
    'male', \
    generate_password_hash('hoge'),\
    'hoge@hoge',\
    datetime.date(1994, 11, 18),\
    '東京都', \
    'ナオキ',\
    'よろしくお願いします',\
    'http://localhost:5000/static/image/test.png',\
    'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry''s standard dummy text ever since the 1500s...',\
    25,\
    48,\
    datetime.datetime(2010, 2, 8, 1, 40, 27, 425337)\
))
cur.execute("INSERT INTO user_web VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}')".format( \
    uuid.uuid4().hex,\
    'male', \
    generate_password_hash('fuga'),\
    'fuga@fuga',\
    datetime.date(1994, 11, 17),\
    '東京都', \
    'ハヤト',\
    'よろしくお願いします',\
    'http://localhost:5000/static/image/test.png',\
    'この文章はダミーです。文字の大きさ、量、字間、行間等を確認するために入れています。',\
    23,\
    46,\
    datetime.datetime.now()\
))

mail_list = ["a@a", "b@b", "c@c", "d@d", "e@e"]
for i in range(5):
    cur.execute("INSERT INTO user_web VALUES ('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}')".format( \
        uuid.uuid4().hex,\
        'male', \
        generate_password_hash('hoge'),\
        mail_list[i],\
        datetime.date(1994, 11, 18),\
        '埼玉県', \
        'ナオキ',\
        'よろしくお願いします',\
        'http://localhost:5000/static/image/test.png',\
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry''s standard dummy text ever since the 1500s...',\
        25,\
        48,\
        datetime.datetime(2010, 2, 8, 1, 40, 27, 425337)\
    ))

# cur.execute("INSERT INTO user_web VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}')".format( \
#     uuid.uuid4().hex,\
#     'female', \
#     'fuga',\
#     'fuga@fuga',\
#     datetime.date(1994, 11, 17),\
#     '東京都', \
#     'まい',\
#     'http://localhost:5000/static/image/test.png',\
#     'この文章はダミーです。文字の大きさ、量、字間、行間等を確認するために入れています。',\
#     25,\
#     46,\
#     datetime.datetime.now()\
# ))

# cur.execute("INSERT INTO user_web VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}')".format( \
#     uuid.uuid4().hex,\
#     'female', \
#     'fuga',\
#     'fuga@fuga',\
#     datetime.date(1994, 11, 17),\
#     '東京都', \
#     'ななせ',\
#     'http://localhost:5000/static/image/test.png',\
#     'この文章はダミーです。文字の大きさ、量、字間、行間等を確認するために入れています。',\
#     23,\
#     46,\
#     datetime.datetime.now()\
# ))


conn.commit()
conn.close()
