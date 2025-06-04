import numpy as np
import matplotlib.pyplot as plt

def interpolate_polynomial_lagrange(points_xy, num_nodes=10):
    x_all = points_xy[:, 0]
    y_all = points_xy[:, 1]

    # Równomiernie wybrane węzły
    idx = np.linspace(0, len(points_xy) - 1, num_nodes, dtype=int)
    x_nodes = x_all[idx]
    y_nodes = y_all[idx]

    # Wartości interpolowane
    x_interp = np.linspace(x_nodes[0], x_nodes[-1], 1000)
    x_interp = np.unique(np.concatenate((x_interp, x_nodes)))
    y_interp = []

    for x in x_interp:
        L = 0
        for i in range(num_nodes):
            li = 1
            for j in range(num_nodes):
                if i != j:
                    li *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
            L += y_nodes[i] * li
        y_interp.append(L)

    points = np.column_stack((x_nodes, y_nodes))
    return x_interp, y_interp, points
def interpolate_polynomial_chebyshev(points_xy, num_nodes=10):
    x_all = points_xy[:, 0]
    y_all = points_xy[:, 1]
    a = x_all.min()
    b = x_all.max()

    # Oblicz węzły Czebyszewa (rosnąco)
    cheb_nodes = 0.5 * (a + b) + 0.5 * (b - a) * np.cos((2 * np.arange(1, num_nodes + 1) - 1) * np.pi / (2 * num_nodes))
    cheb_nodes = cheb_nodes[::-1]

    x_nodes = cheb_nodes
    y_nodes = []

    for x in x_nodes:
        # znajdź dwa punkty (x0, y0), (x1, y1) takie, że x0 <= x <= x1
        for i in range(len(x_all) - 1):
            if x_all[i] <= x <= x_all[i + 1]:
                x0, x1 = x_all[i], x_all[i + 1]
                y0, y1 = y_all[i], y_all[i + 1]
                # interpolacja liniowa w celu określenia y
                y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
                y_nodes.append(y)
                break

    x_interp = np.linspace(a, b, 1000)
    x_interp = np.unique(np.concatenate((x_interp, x_nodes)))
    y_interp = []

    for x in x_interp:
        L = 0
        for i in range(num_nodes):
            li = 1
            for j in range(num_nodes):
                if i != j:
                    li *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
            L += y_nodes[i] * li
        y_interp.append(L)

    points = np.column_stack((x_nodes, y_nodes))
    return x_interp, y_interp, points


def interpolate_spline(points_xy, num_nodes=10):
    # dane wejsciowe - rowniomiernie rozlozone punkty
    indices = np.linspace(0, len(points_xy) - 1, num_nodes, dtype=int)
    points_used = points_xy[indices]

    x = points_used[:, 0]
    y = points_used[:, 1]
    n = len(x) - 1  # liczba przedziałów

    h = [x[i+1] - x[i] for i in range(n)]  # długości przedziałów

    # układ równań dla pochodnych drugiego rzędu
    A = [[0] * (n + 1) for _ in range(n + 1)]
    b = [0] * (n + 1)

    A[0][0] = 1
    A[n][n] = 1

    for i in range(1, n):
        A[i][i - 1] = h[i - 1]
        A[i][i] = 2 * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]
        b[i] = 6 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

    # Rozwiązujemy układ równań A * M = b
    A_np = np.array(A, dtype=float)
    b_np = np.array(b, dtype=float)
    M = np.linalg.solve(A_np, b_np)

    # Obliczanie wartości interpolacji
    x_interp = []
    y_interp = []

    for i in range(n):
        xi, xi1 = x[i], x[i + 1]
        hi = h[i]
        for t in np.linspace(xi, xi1, 50):  # 50 punktów na przedział
            A_i = (xi1 - t) / hi
            B_i = (t - xi) / hi
            C_i = ((A_i**3 - A_i) * hi**2) / 6
            D_i = ((B_i**3 - B_i) * hi**2) / 6
            S_t = A_i * y[i] + B_i * y[i + 1] + C_i * M[i] + D_i * M[i + 1]
            x_interp.append(t)
            y_interp.append(S_t)

    return x_interp, y_interp, points_used