'''
Ejercicio7
Mostrar todos los números impares enetre dos números introducidos por el usuario.

'''
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 < num2:
    for numero in range(num1, num2 + 1):
        if numero % 2 != 0:
            print(numero)
else:
    print("El primer número debe ser menor que el segundo.")
    