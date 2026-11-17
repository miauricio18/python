# 16.61) Botones tipo calculadora

import tkinter as tk

ventana = tk.Tk()
ventana.title("Botones tipo Calculadora")
ventana.geometry("300x225")

leyenda = tk.Label(
    ventana,
    text="Selecciona un boton",
    font=("Arial", 14)
)
leyenda.grid(row=0, column=0, columnspan=2, pady=20)

def mostrar(texto):
    leyenda.config(text="Has pulsado: " + texto)

boton1 = tk.Button(
    ventana,
    text="1",
    font=("Arial", 16),
    width=8,
    height=2,
    command=lambda: mostrar("1")
)

boton2 = tk.Button(
    ventana,
    text="2",
    font=("Arial", 16),
    width=8,
    height=2,
    command=lambda: mostrar("2")
)

boton3 = tk.Button(
    ventana,
    text="3",
    font=("Arial", 16),
    width=8,
    height=2,
    command=lambda: mostrar("3")
)

boton4 = tk.Button(
    ventana,
    text="4",
    font=("Arial", 16),
    width=8,
    height=2,
    command=lambda: mostrar("4")
)

boton1.grid(row=1, column=0, padx=5, pady=5)
boton2.grid(row=1, column=1, padx=5, pady=5)
boton3.grid(row=2, column=0, padx=5, pady=5)
boton4.grid(row=2, column=1, padx=5, pady=5)

ventana.mainloop()
