# 11.56)

import tkinter as tk

def mostrar_letra(letra):
    etiqueta.config(text=f"Presionaste la letra: {letra}")

ventana = tk.Tk()
ventana.title("Ejemplo de grid con botones")
ventana.geometry("300x200")

boton_a = tk.Button(ventana, text="Botón 1", command=lambda: mostrar_letra("A"))
boton_a.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

boton_b = tk.Button(ventana, text="Botón 2", command=lambda: mostrar_letra("B"))
boton_b.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

etiqueta = tk.Label(ventana, text="Presiona un boton", font=("Arial", 14))
etiqueta.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

ventana.mainloop()
