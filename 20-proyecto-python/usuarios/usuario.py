
import datetime # Importar la librería para manejar fechas y horas
import hashlib # Importar la librería para encriptar contraseñas
import usuarios.conexion as conexion # Importar el módulo de conexión a la base de datos

connect = conexion.conectar() # Conectar a la base de datos
cursor = connect[0] # Obtener el cursor de la conexión
database = connect[1] # Obtener la base de datos de la conexión


class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now() # Obtener la fecha y hora actual

        # Encriptar la contraseña usando SHA-256
        cifrado = hashlib.sha256() # Crear objeto de cifrado
        cifrado.update(self.password.encode('utf8')) # Actualizar el objeto con la contraseña codificada en utf8
        sql = "INSERT INTO usuarios VALUES (null, %s, %s, %s, %s, %s)" # Consulta SQL para insertar usuario
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha) # Datos del usuario
                
        try:
            cursor.execute(sql, usuario) # Ejecutar la consulta
            database.commit() # Confirmar los cambios en la base de datos
            
            result = [cursor.rowcount, self] # Devolver el número de filas afectadas y el objeto usuario
            
            cursor.close() # Cerrar el cursor
        except Exception as err:
            print(f'Error: {err}')
            database.rollback() # Deshacer los cambios en caso de error
            result = [0, self]
            cursor.close() # Cerrar el cursor
     
        return result
        
    def identificar(self):
        # Encriptar la contraseña usando SHA-256
        cifrado = hashlib.sha256() # Crear objeto de cifrado
        cifrado.update(self.password.encode('utf8')) # Actualizar el objeto con la contraseña codificada en utf8    
               
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s" # Consulta SQL para identificar usuario
        usuario = (self.email, cifrado.hexdigest()) # Datos del usuario con la contraseña encriptada
        
        cursor.execute(sql, usuario) # Ejecutar la consulta
        result = cursor.fetchone() # Obtener el primer resultado
        
        cursor.close() # Cerrar el cursor
        
        return result
       