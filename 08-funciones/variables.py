'''
Variable local: Variable declarada dentro de una función y solo se puede usar dentro de esa función.
Variable global: Variable declarada fuera de una función y se puede usar en cualquier parte del código.
Para usar una variable global dentro de una función, se debe usar la palabra reservada 'global'.

'''

# Variable global
frase = "Ni los genios son tan genios, ni los mediocres son tan mediocres"

print(frase)

def holaMundo():
    # Variable local
    frase = "Hola mundo"
    print(frase)

    year = 2024
    print(year)

    global website
    website = "www.google.com"
    print(website)

    return "Dato devuelto" + str(year)

print(holaMundo())
print("FUERA",website)
