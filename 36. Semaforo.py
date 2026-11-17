import time
while True:
    # ROJO
    rojo = 1
    amarillo = 0
    verde = 0
    print(rojo, amarillo, verde, "Rojo Detente")
    time.sleep(2)
    
    # VERDE
    rojo = 0
    amarillo = 0
    verde = 1
    print(rojo, amarillo, verde, "VERDE Avanza")
    time.sleep(2)
    
    # AMARILLO
    rojo = 0
    amarillo = 1
    verde = 0
    print(rojo, amarillo, verde, "AMARILLO Precaucion")
    time.sleep(2)
