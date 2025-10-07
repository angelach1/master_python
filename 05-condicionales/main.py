"""
# Condicional if
 SI (if) se cumple una condición, entonces haz algo
 SINO (else) haz otra cosa

if condición:
    hacer algo
else:
    hacer otra cosa

# Operadores de comparación
==  igual
!=  diferente
>   mayor que
<   menor que
>=  mayor o igual que
<=  menor o igual que

# Operadores lógicos
and  Y
or   O
not  NO
! Negación
"""
# Ejemplo 1
print("******************** EJEMPLO 1 ********************")
color = "rojo"
#color = input("Introduce un color: ")

if color == "rojo":
    print("El color es rojo")
else:
    print("El color no es rojo")

# Ejemplo 2
print("\n****************** EJEMPLO 2 ********************")
year = 2020
#year = int(input("Introduce el año actual: "))
if year >= 2021:
    print("Estamos en 2021 o en adelante")
else:
    print("Estamos en 2020 o en años anteriores")

# Ejemplo 3
print("\n****************** EJEMPLO 3 ********************")

nombre = "Victor Robles"
ciudad = "Madrid"
continente = "Europa"
edad = 55
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if continente != "Europa":
        print("No es europeo")
    else:
        print(f"Es europeo y de la ciudad de {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")
    
# Ejemplo 4
print("\n****************** EJEMPLO 4 ********************")

dia = 7
#dia = int(input("Introduce el número del día (1-7): "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("No es un día de la semana")

# Ejemplo 5
print("\n****************** EJEMPLO 5 ********************")
edad_minima = 18
edad_maxima = 65
edad_oficial = 17
#edad_oficial = int(input("Introduce tu edad: "))

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Está en edad de trabajar")
else:
    print("No está en edad de trabajar")
# Otra forma de hacerlo
if not (edad_oficial < edad_minima or edad_oficial > edad_maxima):
    print("Está en edad de trabajar")
else:
    print("No está en edad de trabajar")
# Otra forma más sencilla de hacerlo
if edad_minima <= edad_oficial <= edad_maxima:
    print("Está en edad de trabajar")
else:
    print("No está en edad de trabajar")

# Ejemplo 6
print("\n****************** EJEMPLO 6 ********************")
pais = "España"
#pais = input("Introduce un país: ")
if pais == "México" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")
"""
# Otra forma de hacerlo
if pais in ["México", "España", "Colombia"]:
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")
# Otra forma más sencilla de hacerlo
if pais in ("México", "España", "Colombia"):
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")
# Otra forma aún más sencilla de hacerlo
if pais in {"México", "España", "Colombia"}:
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")
# Otra forma aún más sencilla de hacerlo
if pais in "México España Colombia":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")
# Otra forma aún más sencilla de hacerlo
if pais in "MéxicoEspañaColombia":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")
# Otra forma aún más sencilla de hacerlo
if pais in "MéxicoEspañaColombia":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")
"""
# Ejemplo 7
print("\n****************** EJEMPLO 7 ********************")
pais = "España"
#pais = input("Introduce un país: ")
if pais not in ("México", "España", "Colombia"):
    print(f"{pais} no es un país de habla hispana")
else:
    print(f"{pais} es un país de habla hispana")
    
# Ejemplo 8
print("\n****************** EJEMPLO 8 ********************")
pais = "USA"
if pais != "México" and pais != "España" and pais != "Colombia":
    print(f"{pais} no es un país de habla hispana")
else:
    print(f"{pais} es un país de habla hispana")


