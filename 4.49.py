import tkinter as tk

def saludar():
    print("Hola desde este botón")

ventana = tk.Tk()
ventana.geometry("400x400")
boton = tk.Button(ventana, text="Salúdame", command=saludar)
boton.pack()

ventana.mainloop()
