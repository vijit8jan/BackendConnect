from flask import Flask
import pymysql
import os

app = Flask(__name__)

def get_db_connection():
    connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE()")
        result = cursor.fetchone()
    connection.close()
    return f"Connected to database: {result['DATABASE()']}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
