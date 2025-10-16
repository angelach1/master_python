import os # Módulo para trabajar con el sistema de archivos
import shutil # Módulo para operaciones de alto nivel con archivos y colecciones de archivos

# Crear un directorio
if not os.path.isdir('mi_directorio'):
    os.mkdir('mi_directorio')
    print("Directorio 'mi_directorio' creado.")
else:
    print("El directorio 'mi_directorio' ya existe.")

# Otra forma de crear un directorio
# os.makedirs('mi_directorio/nuevo_directorio', exist_ok=True)
# print("Directorio 'mi_directorio/nuevo_directorio' creado.")
# El parámetro exist_ok=True evita errores si el directorio ya existe
# os.makedirs crea todos los directorios intermedios necesarios
# Si no se especifica exist_ok=True y el directorio ya existe, se lanza un error

# Eliminar un directorio
#os.rmdir('mi_directorio')  
#print("Directorio 'mi_directorio' eliminado.")

# Otra forma de eliminar un directorio
# os.removedirs('mi_directorio/nuevo_directorio')   
# print("Directorio 'mi_directorio/nuevo_directorio' eliminado.")
# os.removedirs elimina todos los directorios intermedios si están vacíos
# Si el directorio no está vacío, se lanza un error
# Si el directorio no existe, se lanza un error
# Si se intenta eliminar un directorio que no está vacío, se lanza un error

## Copiar un directorio

#shutil.copytree('mi_directorio', 'mi_directorio_copiado')
#print("Directorio 'mi_directorio' copiado a 'mi_directorio_copiado'.")
# shutil.copytree copia un directorio y todo su contenido a una nueva ubicación
# Si el directorio de destino ya existe, se lanza un error
# Si el directorio de origen no existe, se lanza un error
# Si el directorio de origen está vacío, se crea un directorio vacío en la ubicación de destino
# Si el directorio de origen contiene archivos y subdirectorios, se copian todos ellos a la ubicación de destino
# Si se intenta copiar un directorio a una ubicación donde no se tienen permisos de escritura, se lanza un error
# Si se intenta copiar un directorio a una ubicación donde ya existe un archivo con el mismo nombre, se lanza un error

# Eliminar un directorio y todo su contenido
# shutil.rmtree('mi_directorio_copiado')
# print("Directorio 'mi_directorio_copiado' eliminado.")
# shutil.rmtree elimina un directorio y todo su contenido de forma recursiva
# Si el directorio no existe, se lanza un error
# Si se intenta eliminar un directorio donde no se tienen permisos de escritura, se lanza un error
# Si se intenta eliminar un directorio que está en uso por otro proceso, se lanza un error
# Si se intenta eliminar un directorio que contiene archivos de solo lectura, se lanza un error
# Si se intenta eliminar un directorio que contiene archivos abiertos, se lanza un error
# Si se intenta eliminar un directorio que contiene enlaces simbólicos, se lanza un error
# Si se intenta eliminar un directorio que contiene archivos protegidos por el sistema, se lanza un error
# Si se intenta eliminar un directorio que contiene archivos ocultos, se lanza un error
# Si se intenta eliminar un directorio que contiene archivos de sistema, se lanza un error
# Si se intenta eliminar un directorio que contiene archivos de configuración, se lanza un error
# Si se intenta eliminar un directorio que contiene archivos temporales, se lanza un error
# Si se intenta eliminar un directorio que contiene archivos de caché, se lanza un error

# Listar el contenido de un directorio
contenido = os.listdir('.') # Lista el contenido del directorio actual
print("Contenido del directorio actual:")
for item in contenido:
    print("-", item)
# os.listdir devuelve una lista con los nombres de los archivos y directorios en el directorio especificado
# Si no se especifica un directorio, se lista el contenido del directorio actual

