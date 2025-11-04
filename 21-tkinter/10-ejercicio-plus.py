"""
CALCULADORA:   
- Dos campos de entrada para números.
- Cuatro botones para las operaciones básicas: suma, resta, multiplicación y división.
- Mostrar el resultado en una alerta

"""
from tkinter import *
from tkinter import messagebox

class Calculadora:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Ejercicio Calculadora con Tkinter")
        self.ventana.geometry("400x400")
        self.ventana.config(bd=25)

        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar() 

        self.marco = Frame(self.ventana, width=250, height=200) # Crear un marco de 250x200 píxeles
        self.marco.config(
            padx=15,
            pady=15,
            bd=5,
            relief="solid"
        )
        self.marco.pack(side="top", anchor="center") # Coloca el marco en la parte superior y centrado
        self.marco.pack_propagate(False) # Evita que el marco se ajuste al tamaño de sus hijos

        Label(self.marco, text="Número 1:").pack()
        Entry(self.marco, textvariable=self.numero1, justify="center").pack()
        Label(self.marco, text="Número 2:").pack()
        Entry(self.marco, textvariable=self.numero2, justify="center").pack()

        Label(self.marco, text="").pack()  # Espacio entre entradas y botones

        Button(self.marco, text="Sumar", command=self.sumar).pack(side="left", fill="x", expand=True)
        Button(self.marco, text="Restar", command=self.restar).pack(side="left", fill="x", expand=True)
        Button(self.marco, text="Multiplicar", command=self.multiplicar).pack(side="left", fill="x", expand=True)
        Button(self.marco, text="Dividir", command=self.dividir).pack(side="left", fill="x", expand=True)

    def cFloat(self, value): # Convertir a float con manejo de errores
        try:
            resultado = float(value)
        except:
            resultado = 0
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")
        return resultado

    def sumar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) + self.cFloat(self.numero2.get())) # Para controlar errores se llama a cFloat
        self.mostrar_resultado()


    def restar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) - self.cFloat(self.numero2.get())) # Para controlar errores se llama a cFloat
        self.mostrar_resultado()

    def multiplicar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) * self.cFloat(self.numero2.get())) # Para controlar errores se llama a cFloat
        self.mostrar_resultado()

    def dividir(self):
        self.resultado.set(self.cFloat(self.numero1.get()) / self.cFloat(self.numero2.get())) # Para controlar errores se llama a cFloat
        self.mostrar_resultado()

    def mostrar_resultado(self):
        messagebox.showinfo("Resultado", f"El resultado es: {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")

    def run(self):
        self.ventana.mainloop()




calculadora = Calculadora()
calculadora.run()