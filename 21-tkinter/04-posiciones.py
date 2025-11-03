from tkinter import *

ventana = Tk()
ventana.geometry("800x600")
texto = Label(ventana, text="¡Hola, bienvenido a Tkinter!")
texto.config(
    fg="white",
    bg="blue",
    font=("Arial", 12),
    padx=20,
    pady=20
)
texto.pack(side=TOP)

texto2 = Label(ventana, text="Esta es mi primera ventana.")
texto2.config(
    height=5,
    width=30,
    fg="yellow",
    bg="red",
    font=("Consolas", 12),
    padx=20,
    pady=20,
    cursor="heart"
)
texto2.pack(side=TOP, fill=X, expand=YES)

texto3 = Label(ventana, text="Texto centrado en la ventana.")
texto3.config(
    height=5,
    width=50,
    fg="green",
    bg="black",
    font=("Terminal", 14, "bold"),
    padx=20,
    pady=20,
    cursor="hand2"
)
texto3.pack(side=LEFT, fill=Y, expand=YES)
texto4 = Label(ventana, text="Texto alineado a la derecha.")
texto4.config(
    height=5,
    width=50,
    fg="blue",
    bg="white",
    font=("Arial", 12),
    padx=20,
    pady=20,
    cursor="arrow"
)
texto4.pack(side=RIGHT, fill=Y, expand=YES)


ventana.mainloop()