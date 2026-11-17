numero_secreto = 7
intento = int(input("Adivina el numero (1-10): "))

while intento != numero_secreto:
    print("incorrecto, intenta otra vez")
    intento = int(input("Adivina el numero (1-10): "))

print("correcto!!")
