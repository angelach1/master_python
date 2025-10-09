'''
FUNCIONES:
- Una función es un bloque de código reutilizable que realiza una tarea específica.
- Se definen utilizando la palabra clave `def`, seguida del nombre de la función y paréntesis.
- Pueden aceptar parámetros (entradas) y devolver valores (salidas).
- Ayudan a organizar el código, mejorar la legibilidad y evitar la repetición.
- Pueden ser llamadas (invocadas) desde cualquier parte del código después de su definición.
- Pueden tener valores predeterminados para sus parámetros.
- Pueden ser anónimas (funciones lambda) para tareas simples.
- Pueden ser recursivas, es decir, llamarse a sí mismas.

def nombre_de_la_funcion(parametro1, parametro2):
    # Bloque de código
    return resultado

'''
'''
# Ejemplo1
print("############## Ejemplo 1 ##############")
# Definición de la función
def muestraNombre():
    print("Victor")
    print("Paco")
    print("Juan")
    print("Francisco")
    print("Aitor")
    print('\n')

# Llamada a la función
muestraNombre()
muestraNombre()
muestraNombre()

# Ejemplo2
print("############## Ejemplo 2 ##############")

# Definición de la función con parámetros
def mostrarTuNombre(nombre, edad):
    print(f'Tu nombre es {nombre}')

    if edad >= 18:
        print('Y eres mayor de edad')

# llamada a la función
nombre = input("Introduce tu nombre: ")
edad = int(input('Introduce tu edad:'))
mostrarTuNombre(nombre, edad)



# Ejemplo 3
print("############## Ejemplo 3 ##############")

def tabla(numero):
    print(f'Tabla de multiplicar del número: {numero}')

    for contador in range(11):
        print(f"{numero} x {contador} = {numero * contador}\n")
        
for i in range(1, 11):
    tabla(i)

    '''

# Ejemplo 4
print("############## Ejemplo 4 ##############")

# Parámetros opcionales en funciones
def getEmpleado(nombre, dni = None):
    print( "EMPLEADO")
    print(f'Nombre: {nombre}')
    if dni != None:
        print(f'DNI: {dni}')

getEmpleado("Ángel Alhambra",)









    