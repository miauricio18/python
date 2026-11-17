import tkinter as tk
ventana = tk.Tk() # Crear la ventana principal
ventana.title("Nombre ventana") # Titulo de la ventana
ventana.geometry("300x200") # Tamaño de la ventana

# Botón salir
boton = tk.Button(ventana, text="Salir", command=ventana.destroy)
boton.pack()

ventana.mainloop()
