import tkinter as tk
from tkinter import messagebox

respuesta = messagebox.askyesno("Confirmación", "¿Desea continuar?")

if respuesta:
    print("continuar")
