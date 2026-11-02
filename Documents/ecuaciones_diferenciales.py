import numpy as np
import math

# Parámetros
h = 0.2
t0 = 0
tf = 1
y0 = 1

# Método de Euler
t = np.arange(t0, tf + h, h)
y = [y0]

for i in range(len(t) - 1):
    y_next = y[i] + h * y[i]
    y.append(y_next)

# Mostrar resultados
print("Método de Euler")
print("t\t y_aprox")

for ti, yi in zip(t, y):
    print(f"{ti:.1f}\t {yi:.4f}")

# Comparación con solución exacta
exacta = math.exp(1)

print("\nSolución exacta en t=1:", round(exacta, 4))
print("Euler en t=1:", round(y[-1], 4))
print("Error absoluto:", round(abs(exacta - y[-1]), 4))