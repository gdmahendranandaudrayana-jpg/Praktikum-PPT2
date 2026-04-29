import matplotlib.pyplot as plt
import numpy as np

# fungsi
def f(x):
    return x**3 - 4*x - 9

a = 2
b = 3

for i in range(6):  # biar gak terlalu banyak
    c = (a*f(b) - b*f(a)) / (f(b) - f(a))

    print("Iterasi", i+1)
    print("a =", a, "b =", b, "c =", c)
    print("------------------")

    # =========================
    # GRAFIK
    # =========================
    x = np.linspace(-1, 5, 100)
    y = f(x)

    plt.figure()

    # grafik fungsi
    plt.plot(x, y, label="f(x)")

    # titik a dan b
    plt.scatter(a, f(a))
    plt.scatter(b, f(b))

    # garis lurus dari a ke b (INI YANG KAMU MAU)
    x_line = np.linspace(a, b, 10)
    y_line = f(a) + (f(b) - f(a)) * (x_line - a) / (b - a)
    plt.plot(x_line, y_line, linestyle="--", label="Garis Regula Falsi")

    # titik c
    plt.scatter(c, 0)

    plt.axhline(0)
    plt.title(f"Iterasi {i+1}")
    plt.legend()
    plt.grid()

    plt.show()

    # update interval
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c