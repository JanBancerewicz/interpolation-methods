import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

heights = pd.read_csv("data/mont_blanc_hike.txt", sep=None, engine='python').get('altitude')
# "Tour du Mont Blanc" - The most beautiful hike in Europe through France, Italy and Switzerland.
# https://www.hikingfex.com/en/post/tour-du-mont-blanc-en


step_distance = round( 181 / (len(heights) - 1), 8)

# Dodanie kolumny z dystansem w km
lengths = np.array([i * step_distance for i in range(len(heights))])

def plot_empty(label, save=False, show=False):
    plt.figure(figsize=(12, 6))
    plt.plot(lengths,heights,  label="Heights (m)", color='blue', markersize=5)
    plt.title("Tour du Mont Blanc - Heights")
    plt.xlabel("Distance (km)")
    plt.ylabel("Height (m)")
    plt.legend()
    plt.grid()


    if save:
        plt.savefig('diagrams/empty_' + label + '.png', dpi=300)

    if show:
        plt.show()

plot_empty("1", save=True, show=True)