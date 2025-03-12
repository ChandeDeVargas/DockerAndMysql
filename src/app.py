from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# Configuración de la conexión a MySQL
db_config = {
    "host": os.getenv("MYSQL_HOST", "db"),
    "user": os.getenv("root", "root"),
    "password": os.getenv("123456789", "root"),
    "database": os.getenv("holamundo", "testdb")
}

@app.route('/')
def hello_world():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"Hola Mundo! Conectado a la BD: {db_name[0]}"
    except Exception as e:
        return f"Error conectando a la base de datos: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
