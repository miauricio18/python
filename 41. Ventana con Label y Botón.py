import tkinter as tk

ventana = tk.Tk()
ventana.title("ventana 1")
ventana.geometry("300x300")

label = tk.Label(ventana, text="Hola mauricio")
label.pack()

boton = tk.Button(ventana, text="Salir", command=ventana.destroy)
boton.pack()

ventana.mainloop()
