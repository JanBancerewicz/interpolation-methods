import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


heights1 = pd.read_csv("data/mont_blanc_hike.txt", sep=None, engine='python').get('altitude')
heights2 = pd.read_csv("data/teide_hike.txt", sep=None, engine='python').get('altitude')
# "Tour du Mont Blanc" - The most beautiful hike in Europe through France, Italy and Switzerland.
# https://www.hikingfex.com/en/post/tour-du-mont-blanc-en


step_distance1 = round( 181 / (len(heights1) - 1), 8)
step_distance2 = round( 30 / (len(heights2) - 1), 8)

# Dodanie kolumny z dystansem w km
lengths1 = np.array([i * step_distance1 for i in range(len(heights1))])
lengths2 = np.array([i * step_distance2 for i in range(len(heights2))])

def normalize(array):
    return 100 * (array - np.min(array)) / (np.max(array) - np.min(array))

lengths1_norm = normalize(lengths1)
heights1_norm = normalize(heights1)

lengths2_norm = normalize(lengths2)
heights2_norm = normalize(heights2)

points_xy1 = np.column_stack((lengths1_norm, heights1_norm))
points_xy2 = np.column_stack((lengths2_norm, heights2_norm))

#TODO
#
#
# metodę wykorzystującą wielomian interpolacyjny Lagrangea,
# oraz metodę wykorzystującą funkcje sklejane trzeciego stopnia.
#
#analiza podstawowa interpolacji wielomianowej 1, 2 - 8 wykresów
    # 10, 20, 50, 100
#analiza podstawowa interpolacji funkcjami sklejanymi 1, 2 - 8 wykresów

    # 10, 20, 50, 100
#analiza dodatkowa 2 - 4 wykresy - węzły chebyszewa

    # 10, 20, 50, 100

#
#