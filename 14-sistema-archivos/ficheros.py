from io import open # Módulo para manejar ficheros
import pathlib # Módulo para manejar rutas de ficheros
import shutil # Módulo para operaciones de ficheros y carpetas
import os # Módulo para operaciones del sistema operativo

# Abrir un archivo (diferentes modos)
# archivo = open("14-sistema-archivos/fichero.txt", "r+") # Lee y escribe
# archivo = open("14-sistema-archivos/fichero.txt", "w+") # Sobreescribe y escribe
# archivo = open("14-sistema-archivos/fichero.txt", "a+") # Añade y escribe
# archivo = open("14-sistema-archivos/fichero.txt", "r") # Solo lectura
# archivo = open("14-sistema-archivos/fichero.txt", "w") # Solo escritura (sobreescribe)
# archivo = open("14-sistema-archivos/fichero.txt", "a") # Solo escritura (añade)
# archivo = open("14-sistema-archivos/fichero.txt") # Por defecto es solo lectura

# Abrir archivo 
ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero.txt"
print(ruta)
archivo = open(ruta, "a+")

# Escribir en el archivo
archivo.write("\nSoy un texto metido desde Python")
for i in range(20):
    archivo.write(f"\nEsta es la Línea número {i}")

# Cerrar archivo
archivo.close()

# Abrir archivo para leer
archivo_lectura = open(ruta, "r")
# Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)


# Leer contenido línea a línea y guardarlo en una lista
lineas = archivo_lectura.readlines()
print(lineas)

print('El número de líneas es: ' + str(len(lineas))) # Imprime el número de líneas

# Imprimir línea a línea en mayusculas
for linea in lineas:
    print(linea.upper())

# Convertir a lista cada línea
for linea in lineas:
    palabras = linea.split()
    print(palabras)


# Cerrar archivo
archivo_lectura.close()

# Copiar un archivo
ruta_origen = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero.txt"
ruta_destino = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_copiado.txt"
shutil.copyfile(ruta_origen, ruta_destino)

# Mover un archivo
ruta_origen = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_copiado.txt"
ruta_destino = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_copiado_nuevo.txt"
shutil.move(ruta_origen, ruta_destino)

# Eliminar un archivo
ruta_destino = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_copiado_nuevo.txt"
if os.path.exists(ruta_destino):
    os.remove(ruta_destino)
else:
    print("No existe el fichero que quieres eliminar")

# Comprobar si un archivo o carpeta existe
ruta_comprobar = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero.txt"
if os.path.exists(ruta_comprobar):
    print("El fichero o carpeta existe")
else:
    print("El fichero o carpeta no existe")