import math

a = 0
b = 3

def f(x):
    return x**6 - 1

m = (a + b) / 2
tolerancia_porcentaje = 0.0001  
error_porcentaje = 100.0        

while error_porcentaje > tolerancia_porcentaje:
    m_ant = m
    fm = f(m)
    fa = f(a)

    print(f"m = {m:.6f}, f(m) = {fm:.6e}, Error = {error_porcentaje:.6f}%")

    if fa * fm < 0:
        b = m
    else:
        a = m

    m = (a + b) / 2
    error_porcentaje = abs((m - m_ant) / m) * 100

print(f"\nLa raíz aproximada es: {m}")
print(f"f(m) = {f(m)}")
print(f"Error porcentual final: {error_porcentaje}%")
