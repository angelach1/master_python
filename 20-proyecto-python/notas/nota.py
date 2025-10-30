import usuarios.conexion as conexion # Importar el módulo de conexión a la base de datos

connect = conexion.conectar() # Conectar a la base de datos
cursor = connect[0] # Obtener el cursor de la conexión
database = connect[1] # Obtener la base de datos de la conexión

class Nota:
    def __init__(self, usuario_id, titulo = '', descripcion = ''): # Constructor de la clase Nota donde le pasamos los atributos obligatorios
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self): # Método para guardar la nota en la base de datos
        sql = "INSERT INTO notas VALUES (null, %s, %s, %s, NOW())" # Consulta SQL para insertar una nota
        nota = (self.usuario_id, self.titulo, self.descripcion) # Datos de la nota

        try:
            cursor.execute(sql, nota) # Ejecutar la consulta
            database.commit() # Confirmar los cambios en la base de datos
            print(f'\nNota guardada: {self.titulo}') # Mensaje de éxito
            return [cursor.rowcount, self] # Devolver el número de filas afectadas y el objeto nota
        
        except Exception as err:
            print(f'Error: {err}') # Mensaje de error
            database.rollback() # Deshacer los cambios en caso de error
            return [0, self] # Devolver 0 filas afectadas y el objeto nota
        
    def mostrar(self): 

        sql = "SELECT * FROM notas WHERE usuario_id = %s"
        cursor.execute(sql, (self.usuario_id))
        resultados = cursor.fetchall()

        for nota in resultados:
            print(f'''
                ***************************  
                ID: {nota[0]}
                Título: {nota[1]}
                Descripción: {nota[2]}
                Fecha: {nota[3]}
                ***************************
            ''')

    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        cursor.execute(sql)
        database.commit()

        if cursor.rowcount >= 1:
            print(f'\nNota/s eliminada/s: {self.titulo}')
        else:
            print(f'\nNo se ha podido eliminar la nota: {self.titulo}')
