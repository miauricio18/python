import random
import time

opciones = ["Premio", "Pierde turno", "Vuelve a intentar", "Dobla puntos", "Pierde todo"]

input("Presiona enter para girar la ruleta...")

i = 0
vueltas = random.randint(10, 20)  # Cuantas veces gira

while i < vueltas:
    print("Girando...", opciones[i % len(opciones)], end="\r")
    time.sleep(0.2)
    i += 1

resultado = opciones[i % len(opciones)]
print("\nLa ruleta cayo en:", resultado)
