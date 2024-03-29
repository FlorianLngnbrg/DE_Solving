# Finite-Differenzen-Methode für ODEs zweiten Grades (Florian Langenberg, 07.03.2024)

import numpy as np
import matplotlib.pyplot as plt

class FDM:
    def __init__(self, m, D, k, y0, v0, time):
        self.m = m
        self.D = D
        self.k = k
        self.y0 = y0
        self.v0 = v0
        self.time = time

    # Berechnung der exakten Lösungsfunktion für die RMS-Fehlerberechnung
    def exact_func(self, x):
        C_1 = self.y0
        C_2 = (self.v0 + (self.D/(2*self.m))*self.y0) / np.sqrt((4*self.m*self.k - self.D**2) / (4*self.m**2))
        return x, np.exp((-self.D)/(2*self.m)*x) * (C_1*np.cos(np.sqrt((4*self.m*self.k-self.D**2)/(4*self.m**2))*x) + C_2*np.sin(np.sqrt((4*self.m*self.k-self.D**2)/(4*self.m**2))*x))

    # FDM für ODEs zweiten Grades. In diesem Fall der DGL des gedämpften Oszillators 
    def calculate_fdm(self, dt):
        knoten = int(self.time / dt)
        t_values = [i * dt for i in range(knoten + 1)]
        y_values = [self.y0]

        v_i = self.v0
        y_i = self.y0

        for i in range(1, knoten + 1):
            v_old = v_i
            y_old = y_i

            v_i = v_old - dt * ((self.D / self.m) * v_old + (self.k / self.m) * y_old)
            y_i = y_old + dt * v_i

            y_values.append(y_i)

        return t_values, y_values

    # RMS-ERROR-Berechnung = sqrt((1/N)*sum(i=1, N, (y_exakt_i-y_approx_i)^2))
    def calculate_rms_error(self, dt):
        t_values, y_values = self.calculate_fdm(dt)
        x_values_exact, y_values_exact = self.exact_func(np.linspace(0, self.time, len(t_values)))
        rms_error = np.sqrt(np.mean((np.array(y_values) - np.array(y_values_exact))**2))
        return rms_error, t_values, y_values, x_values_exact, y_values_exact

class Main:
    def run(self):
        # Grundwerte
        m = 0.4
        k = 2
        # y0 = 0.2
        v0 = 0
        D = 0.1
        time = 10
        dt = 0.1

        # Bei Variationsanwendung immer den Grundwert auskommentieren, der variiert wird!
        y0_values = [-0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4]

        # Entsprechend die Variationsvariable ersetzen, in dem Fall y0.
        print("y0    | RMS-Error")
        for y0 in y0_values:
            fdm = FDM(m, D, k, y0, v0, time)
            rms_error, t_values, y_values, x_values_exact, y_values_exact = fdm.calculate_rms_error(dt)
            print("{:0.2f} | {:0.6f}".format(y0, rms_error))

            # Plot Approx. u. Exakt.
            plt.plot(x_values_exact, y_values_exact, label='Exakte Funktion')
            plt.scatter(t_values, y_values, color='red', label='FDM Punkte')
            plt.xlabel('Zeit (s)')
            plt.ylabel('y-Wert (m)')
            plt.title('Darstellung der berechneten Werte mit 100 (101) Stützpunkten und exakter Funktion')
            plt.grid(True)
            plt.legend()
            plt.show()

if __name__ == "__main__":
    main = Main()
    main.run()