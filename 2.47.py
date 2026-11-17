import tkinter as tk

def mostrar_seleccion():
    seleccion = var.get()
    if seleccion == 1:
        mensaje.config(text="Seleccionaste Python")
    elif seleccion == 2:
        mensaje.config(text="Seleccionaste Java")
    elif seleccion == 3:
        mensaje.config(text="Seleccionaste C++")

ventana = tk.Tk()
ventana.title("Ejemplo de radiobutton")

mensaje = tk.Label(ventana, text="Seleccionaste un lenguaje de programación", font=("Arial", 14))
mensaje.pack(pady=20)

var = tk.IntVar()

rb_python = tk.Radiobutton(ventana, text="Python", variable=var, value=1, font=("Arial", 14))
rb_python.pack()

rb_java = tk.Radiobutton(ventana, text="Java", variable=var, value=2, font=("Arial", 14))
rb_java.pack()

rb_cpp = tk.Radiobutton(ventana, text="C++", variable=var, value=3, font=("Arial", 14))
rb_cpp.pack()

boton = tk.Button(ventana, text="Mostrar Selección", font=("Arial", 14), command=mostrar_seleccion)
boton.pack(pady=20)

ventana.mainloop()
