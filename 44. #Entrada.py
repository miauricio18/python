#Entrada
import tkinter as tk

#función que se ejecuta al presionar el boton
def mostrar_entrada():
    texto_usuario = entrada.get() #obtiene el texto ingresado en el entry
    mensaje.config(text=f"Hola {texto_usuario}!") #muestra el mensaje en el label

#crear la ventana principal
ventana = tk.Tk()
ventana.geometry("300x300")
#configurar el titulo de la ventana
ventana.title("Ejemplo de Entry")

#crear un label para mostrar un mensaje
mensaje = tk.Label(ventana, text="Ingresa tu nombre:", font=("Arial", 14))
mensaje.pack(pady=20)

#crear un entry (campo de texto para que el usuario ingrese algo)
entrada = tk.Entry(ventana, font=("Arial", 14))
entrada.pack(pady=10)

#crear un boton que, al presionarlo, obtendra el texto del entry y lo mostrara
boton = tk.Button(ventana, text="Mostrar saludo", font=("Arial", 14), command=mostrar_entrada)
boton.pack(pady=20)

#iniciar el bucle de eventos de la ventana
ventana.mainloop()
