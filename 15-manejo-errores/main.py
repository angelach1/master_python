# Capturar excepciones y manejar errores de código en Python
# susceptible a fallos/errores.

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    except TypeError:
        return "Error: Los operandos deben ser números."
    else:
        return f"El resultado de {a} dividido por {b} es {resultado}."
    finally:
        print("Operación de división finalizada.")

# Pruebas de la función dividir con diferentes casos
print(dividir(10, 2))  # Caso válido
print(dividir(10, 0))  # Caso de división por cero
print(dividir(10, "a"))  # Caso de tipo incorrecto
print(dividir("x", 2))  # Otro caso de tipo incorrecto
print(dividir(15, 3))  # Otro caso válido
print(dividir(7, -1))  # División con número negativo

# Ejemplo de manejo de errores al buscar un número en una lista
def buscar_numero_en_lista(lista, numero):
    try:
        indice = lista.index(numero)
    except ValueError:
        return f"El número {numero} no se encuentra en la lista."
    else:
        return f"El número {numero} se encuentra en el índice {indice} de la lista."
numeros = [10, 20, 30, 40, 50]
print(buscar_numero_en_lista(numeros, 30))  # Número presente
print(buscar_numero_en_lista(numeros, 60))  # Número ausente    
print(buscar_numero_en_lista(numeros, "a"))  # Tipo incorrecto
print(buscar_numero_en_lista(numeros, 10))  # Otro número presente
print(buscar_numero_en_lista(numeros, -5))  # Número negativo no presente
print(buscar_numero_en_lista(numeros, 50))  # Último número presente
print(buscar_numero_en_lista(numeros, 100))  # Número grande no presente

# Ejemplo de manejo de errores al convertir entrada de usuario a número entero con varias excepciones
def convertir_a_entero(entrada):
    try:
        numero = int(entrada)
    except ValueError:
        return "Error: La entrada no es un número entero válido."
    except TypeError:
        return "Error: La entrada debe ser una cadena o un número."
    except Exception as e:
        return f"Error inesperado: {e} del tipo {type(e).__name__}"
    else:
        return f"La entrada convertida a entero es {numero}."
# Pruebas de la función convertir_a_entero con diferentes entradas
print(convertir_a_entero("123"))  # Entrada válida
print(convertir_a_entero("abc"))  # Entrada no numérica
print(convertir_a_entero(None))  # Entrada None
print(convertir_a_entero(45.67))  # Entrada float
print(convertir_a_entero("456"))  # Otra entrada válida
print(convertir_a_entero([]))  # Entrada lista
print(convertir_a_entero("789xyz"))  # Entrada alfanumérica
print(convertir_a_entero("-100"))  # Entrada número negativo

# Ejemplo de manejo de errores personalizados
try:
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    if edad < 5 or edad > 110:
        raise ValueError("La edad debe estar entre 5 y 110 años.")
    elif len(nombre) < 3:
        raise ValueError("El nombre debe tener al menos 3 caracteres.")
    print(f"Hola {nombre}, tienes {edad} años.")
except ValueError as e:
    print(f"Error de valor: {e}")
    print("Por favor, introduce datos válidos.")
except Exception as e:
    print(f"Error inesperado: {e} del tipo {type(e).__name__}")
except KeyboardInterrupt:
    print("\nOperación cancelada por el usuario.")
except EOFError:
    print("\nNo se recibió entrada del usuario.")
finally:
    print("Programa finalizado.")