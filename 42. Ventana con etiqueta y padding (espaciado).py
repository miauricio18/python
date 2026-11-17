import tkinter as tk

ventana = tk.Tk() # Crear la ventana principal
# Configurar el titulo de la ventana
ventana.title("primera ventana" ) 

# Crear un Label con texto
etiqueta = tk.Label(ventana, text="hola ssss ") 

# Colocar la etiqueta en la ventana
# pady agrega un poco de espacio vertical
etiqueta.pack(pady=20) 

# Iniciar el bucle de eventos en la ventana
ventana.mainloop()
