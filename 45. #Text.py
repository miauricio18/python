#Text
import tkinter as tk

#función que se ejecuta al presionar el boton
def mostrar_texto():
    texto_usuario = campo_texto.get("1.0", "end-1c") #obtiene el texto completo del campo text
    mensaje.config(text= f"Texto ingresado:\n {texto_usuario}") #muestra el texto en el label

#crear la ventana principal
ventana = tk.Tk()

#configurar el titulo de la ventana
ventana.title("Ejemplo de Text")

#crear un label para mostrar un mensaje
mensaje = tk.Label(ventana, text="ingresar algo de texto", font=("Arial", 14))
mensaje.pack(pady=20)

#crear un widget text (area de texto para multiples lineas)
campo_texto = tk.Text(ventana, height=5, width=40, font=("Arial", 14))
campo_texto.pack(pady=10)

#crear un boton que, al presionarlo, obtendra el texto del text y lo mostrara
boton = tk.Button(ventana, text="Mostrar texto", font=("Arial", 14), command=mostrar_texto)
boton.pack(pady=20)

ventana.mainloop()
