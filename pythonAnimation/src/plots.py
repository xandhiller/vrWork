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


def main():
    # Ploting setup
    fig = plt.figure()

#   fig.set_tight_layout(True) # [Causing ERRORS]

    ax = fig.add_subplot(111, projection='3d')
    # No axes, for prettiness
    ax.set_axis_off()
    # Set background to black
    ax.set_facecolor((0.0, 0.0, 0.0))
    # Read in data
    df = pd.read_csv(dataSource) 
    # Pull position from dataframe
    x = df['XX']
    y = df['YY']
    z = df['ZZ']
    # Plot data with small points
    my_plot = ax.scatter(x, y, z, s=1, color='C0')

    k=1
    def _update(k):
      ax.scatter(x,y,z, s=1, color='C0')
      # Make it spin
      ax.view_init(30.0, -45.0 + k)
      # Animation info whilst generating
      label = 'timestep {0}'.format(k)
      print(label)
      return my_plot, ax

    
    def _animate():
        anim = FuncAnimation(fig, _update, frames=np.arange(0, 30))
        anim.save('run.gif',
                  dpi=300,
                  writer='imagemagick')

    # What to actually run
    _animate()
    plt.show()

if __name__ == '__main__':
    main()
