# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

from plotting import *
from approx import *

# from datasource import *

node_nums = [6, 12, 24, 48] # liczba węzłów interpolacji


# wycieczki
plot_trail("1", save=True)
plot_trail("2", save=True)
plt.show()


# interpolacja wielomianowa - równomierna
plot_interpolation("1",1,node_nums[0], save=True)
plot_interpolation("1",1,node_nums[1], save=True)
plot_interpolation("1",1,node_nums[2], save=True)
plot_interpolation("1",1,node_nums[3], save=True)
plt.show()


# interpolacja wielomianowa - równomierna
plot_interpolation("2",1,node_nums[0], save=True)
plot_interpolation("2",1,node_nums[1], save=True)
plot_interpolation("2",1,node_nums[2], save=True)
plot_interpolation("2",1,node_nums[3], save=True)
plt.show()

# interpolacja wielomianowa - Czebyszew
plot_interpolation("1",2,node_nums[0], save=True)
plot_interpolation("1",2,node_nums[1], save=True)
plot_interpolation("1",2,node_nums[2], save=True)
plot_interpolation("1",2,node_nums[3], save=True)
plt.show()

# interpolacja wielomianowa - Czebyszew
plot_interpolation("2",2,node_nums[0], save=True)
plot_interpolation("2",2,node_nums[1], save=True)
plot_interpolation("2",2,node_nums[2], save=True)
plot_interpolation("2",2,node_nums[3], save=True)
plt.show()

# interpolacja funkcjami sklejanymi
plot_interpolation("1",3,node_nums[0], save=True)
plot_interpolation("1",3,node_nums[1], save=True)
plot_interpolation("1",3,node_nums[2], save=True)
plot_interpolation("1",3,node_nums[3], save=True)
plt.show()

# interpolacja funkcjami sklejanymi
plot_interpolation("2",3,node_nums[0], save=True)
plot_interpolation("2",3,node_nums[1], save=True)
plot_interpolation("2",3,node_nums[2], save=True)
plot_interpolation("2",3,node_nums[3], save=True)
plt.show()

