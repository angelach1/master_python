'''
Ejercicio 3: Escribir un programa que compruebe si una variable está vacía y
si está vaciía, rellenarla con texto en minúsculas y mostrarlo en mayúsculas.

'''
variable = "  "
if len(variable.strip()) == 0:
    variable = "texto en minúsculas"
print(variable.upper())