import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conexion = sqlite3.connect("./19-bases-datos/pruebas.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear una tabla
consulta = """
CREATE TABLE IF NOT EXISTS  PRODUCTOS (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    titulo VARCHAR(255),
    descripcion TEXT,
    precio INT,
    fecha TIMESTAMP
);
"""
cursor.execute(consulta)

# Guardar los cambios
conexion.commit()

# Insertar datos en la tabla

consulta = """
INSERT INTO PRODUCTOS (titulo, descripcion, precio, fecha)
VALUES (?, ?, ?, ?);
"""

# Datos a insertar
datos = ("Producto 1", "Descripción del producto 1", 100, "2023-01-01 10:00:00")

# Ejecutar la consulta
cursor.execute(consulta, datos) #Usar parámetros para evitar inyecciones SQL
conexion.commit()

# Consultar datos de la tabla
consulta = "SELECT * FROM PRODUCTOS;"
cursor.execute(consulta)
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)

# Sacar el primer producto
consulta = "SELECT * FROM PRODUCTOS WHERE id = ?;"
cursor.execute(consulta, (1,))
producto = cursor.fetchone()
 
# Borrar todos los productos
#consulta = "DELETE FROM PRODUCTOS;"
#cursor.execute(consulta)
#conexion.commit()

# Insertar varios productos
productos = [
    ("Producto 2", "Descripción del producto 2", 200, "2023-02-01 11:00:00"),
    ("Producto 3", "Descripción del producto 3", 300, "2023-03-01 12:00:00"),
    ("Producto 4", "Descripción del producto 4", 400, "2023-04-01 13:00:00"),
]
consulta = "INSERT INTO PRODUCTOS (titulo, descripcion, precio, fecha) VALUES (?, ?, ?, ?);"
cursor.executemany(consulta, productos) 
conexion.commit()

# Actualizar un producto
consulta = "UPDATE PRODUCTOS SET precio = ? WHERE id = ?;"
cursor.execute(consulta, (250,17))
conexion.commit()   

# Consultar todos los productos
consulta = "SELECT * FROM PRODUCTOS;"
cursor.execute(consulta)
productos = cursor.fetchall()
for producto in productos:
    print(producto)



# Cerrar la conexión
conexion.close()


