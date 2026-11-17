# 12.57) codigo cuatro botones resultado de los botones arriba

import tkinter as tk

def mostrar_letra(letra):
    etiqueta.config(text=f"Presionaste la letra: {letra}")

ventana = tk.Tk()
ventana.title("Ejemplo de grid con botones")
ventana.geometry("300x400")

boton_a = tk.Button(ventana, text="Boton A", command=lambda: mostrar_letra("A"))
boton_a.grid(row=1, column=0, padx=10, pady=10)

boton_b = tk.Button(ventana, text="Boton B", command=lambda: mostrar_letra("B"))
boton_b.grid(row=2, column=0, padx=10, pady=10)

boton_c = tk.Button(ventana, text="Boton C", command=lambda: mostrar_letra("C"))
boton_c.grid(row=1, column=1, padx=10, pady=10)

boton_d = tk.Button(ventana, text="Boton D", command=lambda: mostrar_letra("D"))
boton_d.grid(row=2, column=1, padx=10, pady=10)

etiqueta = tk.Label(ventana, text="Presionaste un boton", font=("Arial", 14))
etiqueta.grid(row=0, column=0, padx=20, pady=20)

ventana.grid_columnconfigure(0, weight=1)

ventana.mainloop()
