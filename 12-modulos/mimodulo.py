
def saludar(nombre):
    return f"Hola, {nombre}"

def calculadora(a, b, operacion):
    if operacion == "sumar":
        return a + b
    elif operacion == "restar":
        return a - b
    elif operacion == "multiplicar":
        return a * b
    elif operacion == "dividir":
        return a / b
    else:
        return "Operación no soportada"
    
    