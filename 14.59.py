# 14.59)
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Menu sencillo")
ventana.geometry("400x300")

def nuevo():
    messagebox.showinfo("Archivo", "Nuevo archivo")

def salir():
    ventana.destroy()

def acerca_de():
    messagebox.showinfo("Acerca de", "Programa creado con tkinter")

barra_menu = tk.Menu(ventana)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

menu_editar = tk.Menu(barra_menu, tearoff=0)
menu_editar.add_command(label="Copiar", command=lambda: print("copiar"))
menu_editar.add_command(label="Pegar", command=lambda: print("pegar"))
barra_menu.add_cascade(label="Editar", menu=menu_editar)

menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

ventana.config(menu=barra_menu)

etiqueta = tk.Label(
    ventana,
    text="Bienvenido a mi programa",
    font=("Arial", 14)
)
etiqueta.pack(pady=80)

ventana.mainloop()
