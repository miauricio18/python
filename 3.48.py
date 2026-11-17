import tkinter as tk

def mostrar_seleccion():
    if var.get() == 1:
        mensaje.config(text="¡La opción está seleccionada!")
    else:
        mensaje.config(text="¡La opción no está seleccionada!")

ventana = tk.Tk()
ventana.title("Ejemplo de Checkbutton")
mensaje = tk.Label(ventana, text="¿Te gusta Python?", font=("Arial", 14))
mensaje.pack(pady=20)

var = tk.IntVar()
check = tk.Checkbutton(ventana, text="Sí, me gusta Python", variable=var, font=("Arial", 14))
check.pack(pady=10)

boton = tk.Button(ventana, text="¡Si, me gusta Python", font=("Arial", 14), command=mostrar_seleccion)
boton.pack(pady=20)

ventana.mainloop()
