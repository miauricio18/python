# 15.60 Lista desplegable

import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Lista desplegable")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Selecciona una opción:")
etiqueta.pack(pady=10)

opciones = ["Python", "Java", "C++", "JavaScript"]

lista = ttk.Combobox(
    ventana,
    values=opciones,
    state="readonly"
)
lista.pack(pady=10)
lista.current(3)

def mostrar_seleccion():
    seleccion = lista.get()
    resultado.config(text=f"Seleccionaste: {seleccion}")

boton = tk.Button(
    ventana,
    text="Aceptar",
    command=mostrar_seleccion
)
boton.pack(pady=10)

resultado = tk.Label(ventana, text="")
resultado.pack(pady=5)

ventana.mainloop()
