#Mensaje
import tkinter as tk

#función que se ejecuta cuando el boton es presionado
def mostrar_mensaje():
    mensaje.config(text="!Has presionado el boton!")

#crear la ventana principal
ventana = tk.Tk()

#configurar el titulo de la ventana
ventana.title("Ejemplo de boton")
ventana.geometry ("500x500")
#crear un boton
boton = tk.Button(ventana, text="!Presioname!", font=("Arial", 14), command=mostrar_mensaje)

#colocar el boton en la ventana
boton.pack(pady=20)

#crear un label para mostrar el mensaje
mensaje = tk.Label(ventana, text="", font=("Arial", 14))
mensaje.pack(pady=20)

#iniciar el bucle de la ventana
ventana.mainloop()
