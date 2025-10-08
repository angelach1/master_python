'''
Ejercicio 9:
Hacer un programa que pida números al usuario
indefinidamente hasta que el usuario ingrese el número 111

'''
while True:
    numero = int(input("Ingrese un número (111 para salir): "))
    if numero == 111:
        print("Has ingresado 111, el programa se detiene.")
        break
    else:
        print(f"Has ingresado el número: {numero}")
        