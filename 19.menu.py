print("--- Menu ---")
print("1. Saludar")
print("2. Sumar dos numeros")
print("3. Salir")

opcion = int(input("Elige una opcion: "))

if opcion == 1:
    print("Hola! Bienvenido")
elif opcion == 2:
    a = int(input("ingresa el primer numero: "))
    b = int(input("ingresa el segundo numero: "))
    print("Resultado:", a + b)
elif opcion == 3:
    print("Saliendo del programa...")
else:
    print("Opcion no valida")
