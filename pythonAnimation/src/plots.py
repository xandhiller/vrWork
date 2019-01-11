################################################################################
# 
# Author: Alex Hiller
# Year: 2019
# Program Description: Generate plots from `pulsarCatalogue.txt`
# 
################################################################################

# Libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
from matplotlib.animation import FuncAnimation
import numpy as np


dataSource = './src/pulsarCatalogue.csv'
saveGifAs = 'run.gif'


def main():
    # Ploting setup
    fig = plt.figure(facecolor='k', edgecolor='k')
    # For no border
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, 
                        wspace=None, hspace=None)
    #fig.set_tight_layout(True) # [Causing ERRORS]
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
    # Position of our sun
    sun = [0, 8.5, 0]
    ax.scatter(sun[0], sun[1], sun[2], 
            s=300, marker='o', zorder=2, edgecolors='r', 
            c='k', linewidths=0.5)
    ax.scatter(x,y,z, s=0.8, color='C0', zorder=1)
    # Plot data with small points
    my_plot = ax

    def _animate():
        k=1 # Used for animation, moves angle incrementally.
        def _update(k):
            # Make it spin
            ax.view_init(30.0 - 2.5*k, 45.0 + 2*k)  # (Φ,θ)
            # Animation info whilst generating
            label = 'timestep {0}'.format(k)
            print(label)
            return my_plot, ax
        anim = FuncAnimation(fig, _update, frames=np.arange(0, 10))
        anim.save(saveGifAs,
                  dpi=300,
                  writer='imagemagick')
                    

    # What to actually run
    ############################################################################ 
    _animate() # Create GIF
    os.system('sxiv -af ' + saveGifAs) # Open with local program
    ############################################################################ 

if __name__ == '__main__':
    main()
