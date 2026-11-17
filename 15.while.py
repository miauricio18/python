num = int(input("ingresa un numero (0 para salir): "))
suma = 0

while num != 0:
    suma += num
    num = int(input("ingresa otro numero (0 para salir): "))

print("La suma total es:", suma)
