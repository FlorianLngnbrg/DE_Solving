import numpy as np
import matplotlib.pyplot as plt

# Konstanten
m = 0.4 # Masse in kg
D = 2 # Federkonstante
k = 0.1 # Dämpfungskonstante

# knoten_liste = [20, 50, 100, 200, 500, 1000, 5000, 10000]

# dt_liste = [0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.002, 0.001]

# zeiten = []

# Randbedingungen
y0 = 0.2
v0 = 0

# print('** Bei 100 Knoten **')
# print('Zeit: ', v0, ' | y-Wert: ', y0)

# Diskretisierung
dt = 0.1
time = 10
knoten = int(time / dt)

# Ergebniswerte
v_i = v0
y_i = y0

# Listen für die Zeit- und y-Werte
t_values = [0]
y_values = [y_i]

# Randwerte
v_i = v0 - dt * ((k/m) * v0 + (D/m) * y0)
y_i = y0 + dt * v0

# if dt == 1:

    # print('Zeit: ', dt, ' | y-Wert: ', y_i)

t_values.append(dt)
y_values.append(y_i)

# Berechnet alle anderen Werte

for i in range(2, knoten+1):
  v_old = v_i
  y_old = y_i

  v_i = v_old - dt * ((k/m) * v_old + (D/m) * y_old)
  y_i = y_old + dt * v_i

  u = dt * i

  # if u.is_integer():

    # print('Zeit: ', u, ' | y-Wert: ', y_i)

  t_values.append(dt * i)
  y_values.append(y_i)

# plt.scatter(t_values, y_values)
# plt.xlabel('Zeit (s)')
# plt.ylabel('y-Wert (m)')
# plt.title('Darstellung der berechneten Werte mit 100 Stützpunkten')
# plt.grid(True)
# plt.show()