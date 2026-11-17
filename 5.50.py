import tkinter as tk

ventana = tk.Tk()
ventana.title("Configuración de elementos")

# bg = color del fondo  fg = color de las letras
label = tk.Label(ventana, text="texto en azul con fuente grande", fg="blue", font=("Arial", 16))
label.pack(pady=10)

boton = tk.Button(ventana, text="Botón rojo", bg="red", fg="white", width=6, height=1)
boton.pack(pady=20)

ventana.mainloop()
