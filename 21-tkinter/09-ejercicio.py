"""
CALCULADORA:   
- Dos campos de entrada para números.
- Cuatro botones para las operaciones básicas: suma, resta, multiplicación y división.
- Mostrar el resultado en una alerta

"""
from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Ejercicio Calculadora con Tkinter")
ventana.geometry("400x400")
ventana.config(bd=25)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar() 

marco = Frame(ventana, width=250, height=200) # Crear un marco de 250x200 píxeles
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief="solid"
)
marco.pack(side="top", anchor="center") # Coloca el marco en la parte superior y centrado
marco.pack_propagate(False) # Evita que el marco se ajuste al tamaño de sus hijos

Label(marco, text="Número 1:").pack()
Entry(marco, textvariable=numero1, justify="center").pack()
Label(marco, text="Número 2:").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()  # Espacio entre entradas y botones

def cFloat(value): # Convertir a float con manejo de errores
    try:
        resultado = float(value)
    except:
        resultado = 0
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")
    return resultado

def sumar():
    resultado.set(cFloat(numero1.get()) + cFloat(numero2.get())) # Para controlar errores se llama a cFloat
    mostrar_resultado()
    
    
def restar():
    resultado.set(cFloat(numero1.get()) - cFloat(numero2.get())) # Para controlar errores se llama a cFloat
    mostrar_resultado()

def multiplicar():
    resultado.set(cFloat(numero1.get()) * cFloat(numero2.get())) # Para controlar errores se llama a cFloat
    mostrar_resultado()
    
def dividir():
    resultado.set(cFloat(numero1.get()) / cFloat(numero2.get())) # Para controlar errores se llama a cFloat
    mostrar_resultado()

def mostrar_resultado():
    messagebox.showinfo("Resultado", f"El resultado es: {resultado.get()}") 
    numero1.set("")
    numero2.set("")

Button(marco, text="Sumar", command=sumar).pack(side="left", fill="x", expand=True)
Button(marco, text="Restar", command=restar).pack(side="left", fill="x", expand=True)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill="x", expand=True)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill="x", expand=True)




ventana.mainloop()

