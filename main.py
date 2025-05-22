import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from plotting import *

heights1 = pd.read_csv("data/mont_blanc_hike.txt", sep=None, engine='python').get('altitude')
heights2 = pd.read_csv("data/teide_hike.txt", sep=None, engine='python').get('altitude')
# "Tour du Mont Blanc" - The most beautiful hike in Europe through France, Italy and Switzerland.
# https://www.hikingfex.com/en/post/tour-du-mont-blanc-en


step_distance1 = round( 181 / (len(heights1) - 1), 8)
step_distance2 = round( 30 / (len(heights2) - 1), 8)

# Dodanie kolumny z dystansem w km
lengths1 = np.array([i * step_distance1 for i in range(len(heights1))])
lengths2 = np.array([i * step_distance2 for i in range(len(heights2))])


def plot_empty(label, save=False, show=False):
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
        plt.savefig('diagrams/empty_' + label + '.png', dpi=300)

    if show:
        plt.show()

plot_empty("2", save=True, show=True)