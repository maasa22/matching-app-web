import config
import psycopg2

user = config.user
password = config.password
host = config.host
port_db = config.port_db
database = config.database

conn = psycopg2.connect("postgresql://{}:{}@{}:{}/{}".format(user, password, host, port_db, database))
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS user_m")
cur.execute('''CREATE TABLE user_m \
                (id_user_M text, \
                password text,\
                mail text, \
                birthday text, \
                display_name text, \
                self_images text, \
                self_introduction text, \
                favorites text, \
                last_login text \
                )''')

cur.execute("DROP TABLE IF EXISTS user_f")
cur.execute('''CREATE TABLE user_f \
                (id_user_f text, \
                password text,\
                mail text, \
                birthday text, \
                display_name text, \
                self_images text, \
                self_introduction text, \
                favorites text, \
                last_login text \
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

conn.commit()
conn.close()
