import numpy as np
import matplotlib.pyplot as plt
import time as tm

# Die Zeit wird insgesamt fünf mal gemessen und dann durch fünf dividiert (Durchschnitt). So reduziert man minimale Messungenauigkeiten 
# einzelner Durchführungen verursacht durch den Computer selbst.

# Konstanten
m = 0.4 # Masse in kg
D = 0.1   # Federkonstante
k = 2 # Dämpfungskonstante

# Randbedingungen
y0 = 0.2
v0 = 0

# Diskretisierung
dt = 0.00001
time = 10

# Start der Zeitmessung:

start_zeit = tm.time()
for j in range(0, 4):

    # Knotenberechnung
    knoten = int(time / dt)

    # Ergebniswerte
    v_i = v0
    y_i = y0

    # Listen für die Zeit- und y-Werte
    t_values = [0]
    y_values = [y_i]

    # Randwerte
    v_i = v0 - dt * ((D/m) * v0 + (k/m) * y0)
    y_i = y0 + dt * v0

    t_values.append(dt)
    y_values.append(y_i)

    # Berechnet die Randwerte
    for i in range(2, knoten+1):
        v_old = v_i
        y_old = y_i

        v_i = v_old - dt * ((k/m) * v_old + (D/m) * y_old)
        y_i = y_old + dt * v_i

        t_values.append(dt * i)
        y_values.append(y_i)

# Endzeit messen
end_zeit = tm.time()

# Gesamtzeit berechnen und in Millisekunden umwandeln und dann durch 5 teilen
gesamtzeit_ms = ((end_zeit - start_zeit) * 1000) / 5

print('Zeit für 100 Knoten:', gesamtzeit_ms, 'Millisekunden')