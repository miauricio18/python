# 10.55
import tkinter as tk

def mostrar_a():
    etiqueta.config(text="A")

def mostrar_b():
    etiqueta.config(text="B")

ventana = tk.Tk()
ventana.title("Ejemplo de grid con botones")
ventana.geometry("300x150")

boton_a = tk.Button(ventana, text="Botón 1", command=mostrar_a)
boton_a.grid(row=0, column=0, padx=20, pady=20)

boton_b = tk.Button(ventana, text="Botón 2", command=mostrar_b)
boton_b.grid(row=0, column=1, padx=20, pady=20)

etiqueta = tk.Label(ventana, text="", font=("Arial", 24, "bold"))
etiqueta.grid(row=1, column=0, columnspan=2, pady=10)

ventana.mainloop()
