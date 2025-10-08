'''
Ejercicio 10:
Hacer un programa que pida la nota de 15 alumnos y sacar por pantalla cuantos han aprobado y cuantos han suspendido.

'''
aprobados = 0
suspendidos = 0
for i in range(15):
    nota = float(input(f"Ingrese la nota del alumno {i+1}: "))
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
print(f"Cantidad de alumnos aprobados: {aprobados}")
print(f"Cantidad de alumnos suspendidos: {suspendidos}")

# Hacer lo mismo con un bucle while pero preguntando cuantos alumnos hay
num_alumnos = int(input("Ingrese la cantidad de alumnos: "))
aprobados = 0
suspendidos = 0
contador = 0
while contador < num_alumnos:
    nota = float(input(f"Ingrese la nota del alumno {contador+1}: "))
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
    contador += 1
print(f"Cantidad de alumnos aprobados: {aprobados}")
print(f"Cantidad de alumnos suspendidos: {suspendidos}")

