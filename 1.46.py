import tkinter as tk
ventana=tk.Tk()

ventana.title("Ejemplo de frame")

frame1=tk.Frame(ventana,bg ="lightblue",bd=5)
frame1.pack(padx=20, pady=20)

Label1=tk.Label(frame1, text="Este es un frame", font=("Arial", 14))
Label1.pack(pady=20)

frame2=tk.Frame(frame1, bg="lightgreen", bd=3)
frame2.pack(pady=20)

label2=tk.Label(frame2,text="Este es un frame dentro del primero", font=("Arial",14))
label2.pack(pady=20)

boton1=tk.Button(frame1,text="Haz click aqui", font=("Arial",14))
boton1.pack(pady=10)

ventana.mainloop()
