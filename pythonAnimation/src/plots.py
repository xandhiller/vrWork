################################################################################
# 
# Author: Alex Hiller
# Year: 2019
# Program Description: Generate plots from `pulsarCatalogue.csv`
# 
################################################################################ 
# Libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np
from math import ceil


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
    x   = df['XX']
    y   = df['YY']
    z   = df['ZZ']
    col = df['DISC_DATE']
    # Position of our sun
    sun = [0, 8.5, 0]
#    ax.scatter(x,y,z, s=0.5, c=df.DISC_DATE, zorder=1)

    # Get array of years
    years = []
    for i,el in enumerate(df.DISC_DATE):
        if el not in years:
            years.append(el)
    years.sort()

    for year in years:
        print(year)

    year_increment = 20

    bottom = min(years)
    upper = min(years) + year_increment 
    top = max(years)
    intervals = ceil(len(years)/year_increment )
    # Plot each series of years 
    for interval in range(intervals):
        _x,_y,_z = [],[],[]
        _df = df[df.DISC_DATE <= upper]
        _df = _df[_df.DISC_DATE >= bottom]
        _x = list(_df['XX'].values)
        _y = list(_df['YY'].values)
        _z = list(_df['ZZ'].values)
        _label = str(bottom) + ' - ' + str(upper)
        ax.scatter(_x, _y, _z, label=_label, s=0.5, alpha=0.5) 

        # Update year interval
        bottom += year_increment  
        if upper + year_increment  < top:
            upper += year_increment 
        else:
            upper = top
            

    ax.legend()
                   
    ax.scatter(sun[0], sun[1], sun[2], 
           s=500, marker='o', zorder=2, edgecolors='r', alpha=0.5,
           c='orange', linewidths=0.5, label='You are here.')
    # Plot data with small points
    my_plot = ax

    def _animate():
        k=1 # Used for animation, moves angle incrementally.
        def _update(k):
            # Make it spin
            ax.view_init(30.0 , 45.0 + k)  # (Φ,θ)
            # Animation info whilst generating
            label = 'timestep {0}'.format(k)
            print(label)
            return my_plot, ax
        anim = FuncAnimation(fig, _update, frames=np.arange(0, 360))
        anim.save(saveGifAs,
                  dpi=300,
                  writer='imagemagick')
                    

    # What to actually run
    ############################################################################ 
    plt.show()
#    _animate() # Create GIF
    os.system('sxiv -af ' + saveGifAs) # Open with local program
    ############################################################################ 

if __name__ == '__main__':
    main()
