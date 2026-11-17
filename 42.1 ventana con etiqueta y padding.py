import tkinter as tk

ventana = tk.Tk() # Crear la ventana principal
# Configurar el titulo de la ventana
ventana.title("primera ventana" ) 
ventana.geometry("400x400")
# Crear un Label con texto
etiqueta = tk.Label(ventana, text="hola ssss ", font=("arial",16))


# Colocar la etiqueta en la ventana
# pady agrega un poco de espacio vertical
etiqueta.pack(pady=170) 

# Iniciar el bucle de eventos en la ventana
ventana.mainloop()
