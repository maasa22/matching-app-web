### insert_dummy_data.pyに合わせて修正する。

import config
import psycopg2

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
                gender text, \
                password text,\
                mail text, \
                birthday date, \
                display_name text, \
                self_status_message text, \
                self_images text, \
                self_introduction text, \
                favorites numeric, \
                last_login timestamp \
                )''')

cur.execute("DROP TABLE IF EXISTS chat")
cur.execute('''CREATE TABLE chat \
                (id_chat text, \
                text_chat text,\
                sender_id text, \
                receiver_id text \
                )''')

cur.execute("DROP TABLE IF EXISTS favorites")
cur.execute('''CREATE TABLE favorites \
                (id_favorites text, \
                time_favorites text,\
                sender_id text, \
                receiver_id text \
                )''')

# - matches(batch)
#   - id_matches
#   - user_M
#   - user_F

conn.commit()
conn.close()
