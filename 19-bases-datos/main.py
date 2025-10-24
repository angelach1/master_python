import mysql.connector

# Conexión a la base de datos
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="master_python"
)
# ¿La conexión fue exitosa?
if database.is_connected():
    print("Conexión exitosa a la base de datos MySQL")

# Crear un cursor para ejecutar comandos SQL
cursor = database.cursor(buffered=True)

# Crear una base de datos llamada 'master_python'
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
print("Base de datos 'master_python' creada o ya existente")

# Listar todas las bases de datos
cursor.execute("SHOW DATABASES")
print("Bases de datos disponibles:")
for db in cursor:
    print(db)
    print("Base de datos disponible:", db[0])

# Crear tablas en la base de datos 'master_python' de vehículos
cursor.execute("USE master_python")
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos (
    id INT(10) AUTO_INCREMENT,
    marca VARCHAR(40),
    modelo VARCHAR(100),
    anio INT(4),
    precio FLOAT(10,2),
    CONSTRAINT pk_vehiculo PRIMARY KEY (id)
)
""")
 # Confirmar la creación de la tabla
database.commit()

# Listar todas las tablas en la base de datos 'master_python' y describir la tabla 'vehiculos'
cursor.execute("SHOW TABLES")
print("Tablas en la base de datos 'master_python':")
for table in cursor:
    print("Tabla disponible:", table[0])
cursor.execute(f"DESCRIBE {table[0]}")
for column in cursor:
    print("Columna:", column[0], "Tipo:", column[1])

'''
# Insertar datos en la tabla 'vehiculos'. El id es auto_incremental por lo que no se incluye en la inserción
vehiculos = [
    ("Toyota", "Corolla", 2020, 20000.00),
    ("Ford", "Mustang", 2021, 30000.00),
    ("Chevrolet", "Camaro", 2019, 25000.00)
]
insert_query = "INSERT INTO vehiculos (marca, modelo, anio, precio) VALUES (%s, %s, %s, %s)" # Consulta parametrizada
cursor.executemany(insert_query, vehiculos) # Insertar múltiples registros
print(f"{cursor.rowcount} registros insertados en la tabla 'vehiculos'")
database.commit()
'''

# Actualizar datos en la tabla 'vehiculos'
update_query = "UPDATE vehiculos SET precio = %s WHERE marca = %s"
new_price = (22000.00, "Toyota")
cursor.execute(update_query, new_price)
database.commit()
print(f"{cursor.rowcount} registro(s) actualizado(s) en la tabla 'vehiculos'")

# Eliminar datos de la tabla 'vehiculos'
delete_query = "DELETE FROM vehiculos WHERE marca = %s"
brand_to_delete = ("Ford",)
cursor.execute(delete_query, brand_to_delete)
database.commit()
print(f"{cursor.rowcount} registro(s) eliminado(s) de la tabla 'vehiculos'")

# Consultar datos de la tabla 'vehiculos'
cursor.execute("SELECT * FROM vehiculos")
resultados = cursor.fetchall()
print("Datos de la tabla 'vehiculos':")
for fila in resultados:
    print(fila)
    print("Marca:", fila[1])
    print("Modelo:", fila[2])
    print("Año:", fila[3])
    print("Precio:", fila[4])
    print("-----------------------")


# Cerrar el cursor y la conexión
cursor.close()
database.close()
print("Conexión cerrada")