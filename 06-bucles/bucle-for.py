"""
# Bucles for

# Sintaxis:
# for variable in elemento_iterable (secuencia, rango, etc.):
#     bloque de código
#     ...

"""
# Ejemplo 1: Iterar sobre una range de números
contador = 0
resultado = 0

for contador in range(0, 10):
    print("voy por el número " + str(contador))
    resultado += contador
print("El resultado es " + str(resultado))
print("-----")

# Ejemplo 2: tablas de multiplicar
print("\nTablas de multiplicar")

numero_usuario = int(input("¿De qué número quieres la tabla? "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"Tabla de multiplicar del {numero_usuario}" )

for numero_tabla in range(1, 11):

    if numero_usuario == 45:
        print("No se permiten las tablas del 45")
        break # Sale del bucle

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print("Tabla finalizada")
print("-----")

