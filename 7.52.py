import matplotlib.pyplot as plt

# Coordenadas
x = [1, 7]
y = [3, 9]

plt.figure(figsize=(6, 6))
plt.plot(x, y, 'ro', markersize=10)

# Etiquetas sobre los puntos
plt.text(x[0] + 0.1, y[0] + 0.1, f"({x[0]}, {y[0]})", fontsize=12)
plt.text(x[1] + 0.1, y[1] + 0.1, f"({x[1]}, {y[1]})", fontsize=12)

plt.title("Gráfico de dos puntos (x, y)")
plt.xlabel("Eje x")
plt.ylabel("Eje y")

plt.xlim(0, 10)
plt.ylim(0, 10)

# Cuadrícula
plt.grid(True)

# Mostrar gráfica
plt.show()
