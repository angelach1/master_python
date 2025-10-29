import mysql.connector # Importar la librería para conectar con MySQL

def conectar():
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='master_python',
        port=3306
    ) # Puerto por defecto de MySQL es 3306

    cursor = database.cursor(buffered=True) # Cursor para ejecutar consultas
    return [cursor, database]