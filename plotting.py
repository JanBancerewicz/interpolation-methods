import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import approx
from datasource import *

ranges = [-20, 120]

def plot_trail(label, save=False):
    x = lengths1 if label=="1" else lengths2
    y = heights1 if label=="1" else heights2
    name = "Tour du Mont Blanc - Heights" if label=="1" else "Pico del Teide volcano tour - Heights"

    plt.figure(figsize=(12, 6))
    plt.plot(x,y,  label="Height (m)", color='blue', markersize=5)
    plt.title(name)
    plt.xlabel("Distance (km)")
    plt.ylabel("Height (m)")
    plt.legend()
    plt.grid()

    if save:
        plt.savefig('diagrams/trail_' + label + '.png', dpi=300)


def plot_interpolation(label: str, method: int, num_nodes=10, save=False): # 24 wykresow z tego
    points_xy = points_xy1 if label == "1" else points_xy2 # label 1 or 2
    x_all, y_interp, points = approx.interpolate_polynomial_lagrange(points_xy, num_nodes) if method == 1 else approx.interpolate_polynomial_chebyshev(points_xy, num_nodes) if method == 2 else approx.interpolate_spline(points_xy, num_nodes)
    name = "lagrange" if method == 1 else "chebyshev" if method == 2 else "spline" # name 1 or 2 or 3


    plt.figure(figsize=(12, 6))
    plt.ylim(ranges[0], ranges[1])
    plt.plot(points_xy[:, 0], points_xy[:, 1], label='Original Path', color='blue')
    plt.plot(x_all, y_interp, label='Interpolated Path', color='red', linestyle='-', linewidth=1)
    plt.scatter(points[:, 0], points[:,1], color="green", label="Chosen nodes", zorder=5, marker='.')
    plt.legend()
    plt.title('Polynomial Interpolation of path '+ label + '. Number of nodes: ' + str(num_nodes)+', '+name+' method')
    plt.xlabel('Scaled length (%)')
    plt.ylabel('Scaled height (%)')
    plt.grid(True)

    if save:
        plt.savefig('diagrams/interpolation_'+name+'_' + str(num_nodes) + "_" + label + '.png', dpi=300)

