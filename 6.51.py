import matplotlib.pyplot as plt

# Coordenadas
x = 3
y = 5

# Crear gráfica
plt.figure(figsize=(6, 6))
# 'ro' = red + circle
plt.plot(x, y, 'ro', markersize=10)

# Añadir etiquetas
plt.title("Gráfico de un punto (x, y)")
plt.xlabel("Eje x")
plt.ylabel("Eje y")

# Límites gráficos para que el punto se vea bien
plt.xlim(0, 10)
plt.ylim(0, 10)

# Cuadrícula (opcional)
plt.grid(True)

# Mostrar la gráfica
plt.show()
