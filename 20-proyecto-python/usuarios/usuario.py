import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='master_python'
    port=3306
) # Puerto por defecto de MySQL es 3306

cursor = database.cursor(buffered=True) # Cursor para ejecutar consultas

class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

   def registrar(self):
        print(f'\nPerfecto {self.nombre}, ya estás registrado en el sistema!!')
        return self.nombre

    def identificar(self):
        print(f'\nBienvenido de nuevo {self.nombre}!!')
        return self.nombre