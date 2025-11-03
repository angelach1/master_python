from tkinter import *
ventana = Tk()
ventana.geometry("800x600")
ventana.config(
    bg="lightgray",
    bd=50
)

def recoger_dato():
    resultado.set(dato.get()) # asigna a la variable resultado el valor recogido en dato

dato = StringVar() # variable para almacenar el dato recogido
resultado = StringVar() # variable para almacenar el resultado

Label(ventana, text="Mete un texto y luego lo recogeremos",
    fg="black",
    bg="lightgray",  
    font=("Open Sans", 10, "bold"),
    bd=5
).pack(anchor=NW)

Entry(ventana, textvariable=dato).pack(anchor=NW) # campo de entrada de texto. textvariable vincula el valor del campo a la variable dato

Label(ventana, text="Dato recogido: ").pack(anchor=NW) # salto de línea
texto_recogido = Label(ventana, textvariable=resultado)
texto_recogido.config(
    fg="blue",
    bg="lightgray",
    font=("Arial", 12),
    justify="left"
)
texto_recogido.pack(anchor=NW) # etiqueta para mostrar el dato recogido

Button(ventana, text="Recoger dato", command=recoger_dato).pack(anchor=NW) # botón para recoger el dato

ventana.mainloop()