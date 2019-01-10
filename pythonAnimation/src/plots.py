################################################################################
# 
# Author: Alex Hiller
# Year: 2019
# Program Description: Generate plots from `pulsarCatalogue.txt`
# 
################################################################################

# Libraries
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
from matplotlib.animation import FuncAnimation
import numpy as np

dataSource = './src/pulsarCatalogue.csv'


#   plt.show()


def main():
    # Ploting setup
    fig = plt.figure()
    fig.set_tight_layout(True)
    ax = fig.add_subplot(111, projection='3d')
    # Read in data
    df = pd.read_csv(dataSource) 
    # Pull position from dataframe
    x = df['XX']
    y = df['YY']
    z = df['ZZ']
    # Plot data with small points

    ax.scatter(x,y,z, s=1)

    # No axes, for prettiness
    ax.set_axis_off()
    # Set background to black
#    ax.set_facecolor((0.0, 0.0, 0.0))
    # Pop up the window with the result

#       for angle in range(0, 360):
#           ax.view_init(30, angle)
#           plt.draw()
#           plt.pause(.01)

    k=1
    my_plot = ax.scatter(x[:k], y[:k], z[:k], color='C0')
    def update(k):
       # Make it spin
       ax.view_init(30.0, -45.0 + k)
       # Animation info whilst generating
       ax.scatter(x,y,z, s=1)
       label = 'timestep {0}'.format(k)
       print(label)
       return my_plot, ax
    anim = FuncAnimation(fig, update, frames=np.arange(0, 360))
    anim.save('test.gif',
               dpi=40, 
               writer='imagemagick')
    plt.show()

# TODO
# simple animation with spin


if __name__ == '__main__':
    main()
