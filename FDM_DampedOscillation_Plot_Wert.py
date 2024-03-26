import numpy as np

class FDM:
    def __init__(self, m, D, k, y0, v0, time):
        self.m = m
        self.D = D
        self.k = k
        self.y0 = y0
        self.v0 = v0
        self.time = time

    def exact_func(self, x):
        C_1 = self.y0
        C_2 = (self.v0 + (self.D/(2*self.m))*self.y0) / np.sqrt((4*self.m*self.k - self.D**2) / (4*self.m**2))
        return np.exp((-self.D)/(2*self.m)*x) * (C_1*np.cos(np.sqrt((4*self.m*self.k-self.D**2)/(4*self.m**2))*x) + C_2*np.sin(np.sqrt((4*self.m*self.k-self.D**2)/(4*self.m**2))*x))

    def calculate_fdm(self, dt):
        knoten = int(self.time / dt)
        t_values = [i * dt for i in range(knoten + 1)]
        y_values = [self.y0]

        v_i = self.v0
        y_i = self.y0

        for i in range(1, knoten + 1):
            v_old = v_i
            y_old = y_i

            v_i = v_old - dt * ((self.k / self.m) * v_old + (self.D / self.m) * y_old)
            y_i = y_old + dt * v_i

            y_values.append(y_i)

        return t_values, y_values

    def calculate_rms_error(self, dt):
        t_values, y_values = self.calculate_fdm(dt)
        x_values_exact = np.linspace(0, self.time, len(t_values))
        y_values_exact = self.exact_func(x_values_exact)
        rms_error = np.sqrt(np.mean((np.array(y_values) - np.array(y_values_exact))**2))
        return rms_error

class Main:
    def run(self):
        # Grundwerte
        m = 0.4
        k = 2
        y0 = 0.2
        v0 = 0
        D = 0.1
        time = 10
        #dt = 0.1

        dt_values = [1.0, 0.5, 0.25, 0.2, 0.15, 0.10, 0.05, 0.02, 0.01]

        print("D    | RMS-Error")
        for dt in dt_values:
            fdm = FDM(m, D, k, y0, v0, time)
            rms_error = fdm.calculate_rms_error(dt)
            print("{:0.2f} | {:0.6f}".format(dt, rms_error))



if __name__ == "__main__":
    main = Main()
    main.run()





















"""
# Konstanten
m = 0.4 # Masse in kg
D = 2 # Federkonstante
k = 0.1 # Dämpfungskonstante

# Randbedingungen
y0 = 0.2
v0 = 0

# Diskretisierung
dt = 0.01
time = 10
knoten = int(time / dt)

# Ergebniswerte
v_i = v0
y_i = y0

# Listen für die Zeit- und y-Werte der FDM
t_values = [0]  # Anfangszeitpunkt
y_values = [y_i]  # Anfangswert

# Berechnet alle anderen Werte der FDM
for i in range(1, knoten+1):  # Starte von 1, da der Anfangswert bereits vorhanden ist
    v_old = v_i
    y_old = y_i

    v_i = v_old - dt * ((k/m) * v_old + (D/m) * y_old)
    y_i = y_old + dt * v_i

    t_values.append(dt * i)
    y_values.append(y_i)

# Exakte Funktion
exact_func = lambda x: np.exp((-0.1)/(2*0.4)*x) * (0.2*np.cos(np.sqrt((4*0.4*2-(0.1)**2)/(4*(0.4)**2))*x) + 0.011198*np.sin(np.sqrt((4*0.4*2-(0.1)**2)/(4*(0.4)**2))*x))

# Feineres Gitter für die exakte Funktion
x_values_exact = np.linspace(0, time, 1000)
y_values_exact = exact_func(x_values_exact)

#print("Stelle | FDM-Wert | Exakter Wert | Fehler (Differenz)")
#for i, t in enumerate(t_values[1:], start=1):
 #   if t.is_integer():
 #       x_exact = exact_func(t)
  #      error = np.abs(y_values[i] - x_exact)
  #      print("{:.1f}    | {:.4f}     | {:.4f}      | {:.4f}".format(t, y_values[i], x_exact, error))


# Plot
# plt.plot(x_values_exact, y_values_exact, label='Exakte Funktion')
# plt.scatter(t_values, y_values, color='red', label='FDM Punkte')
# plt.xlabel('Zeit (s)')
# plt.ylabel('y-Wert (m)')
# plt.title('Darstellung der berechneten Werte mit 100 (101) Stützpunkten und exakter Funktion')
# plt.grid(True)
# plt.legend()
# plt.show()

"""