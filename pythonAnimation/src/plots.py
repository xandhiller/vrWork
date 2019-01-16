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



class pulsarPlot:
    def __init__(self):
        # All variables used to tune the plots
        self.dataSource = './src/pulsarCatalogue.csv'
        self.filename = 'run.gif'
        self.df     = pd.read_csv(self.dataSource) 
        self.x      = self.df['XX']
        self.y      = self.df['YY']
        self.z      = self.df['ZZ']
        self.date   = self.df['DISC_DATE']
        self.sun    = [0, 8.5, 0]
        self.years  = self.getYears()
        self.fig    = plt.figure(facecolor='k', edgecolor='k')
        self.ax     = self.fig.add_subplot(111, projection='3d')
        self.ax.set_axis_off()
        self.ax.set_facecolor((0.0, 0.0, 0.0))
        self.year_increment = 20
        self.nbFrames = np.arange(0, 10)
        self.plotOurSun = True
        self.show = True
        self.fig.subplots_adjust(left=0, bottom=0, right=1, top=1, 
                        wspace=None, hspace=None)

    # Generate a list of years to use as an x-axis variable.
    def getYears(self):
        years = []
        for i,el in enumerate(self.df.DISC_DATE):
            if el not in years:
                years.append(el)
        years.sort()
        return years

    # Plot (with colour) the years of discovery of pulsars
    def plotYears(self):
        # Arithmetic for generating year intervals
        bottom = min(self.years)
        upper = min(self.years) + self.year_increment 
        top = max(self.years)
        intervals = ceil(len(self.years)/self.year_increment)
        # Plot each series of years 
        for interval in range(intervals):
            _x,_y,_z = [],[],[]
            # Truncate year values
            _df = self.df[self.df.DISC_DATE <= upper]
            _df = _df[_df.DISC_DATE >= bottom]
            # Format df for plotting
            _x = list(_df['XX'].values)
            _y = list(_df['YY'].values)
            _z = list(_df['ZZ'].values)
            # Generate label for legend
            _label = str(bottom) + ' - ' + str(upper)         
            # Actually plot it.
            self.ax.scatter(_x, _y, _z, label=_label, s=0.5, alpha=0.5)  
            # Update year interval
            bottom += self.year_increment  
            if upper + self.year_increment  < top:
                upper += self.year_increment 
            else:
                upper = top
        if self.plotOurSun == True:
            self.ax.scatter(self.sun[0], self.sun[1], self.sun[2], 
                   s=500, marker='o', zorder=2, edgecolors='r', alpha=0.5,
                   c='orange', linewidths=0.5, label='You are here.')
        # Show the legend
        self.ax.legend()

    def animateSpin(self):
        my_plot = self.ax
        k=1 # Variable used for animation, moves angle incrementally.
        def _update(k):
            # Make it spin
            self.ax.view_init(30.0 , 45.0 + k)  # (Φ,θ)
            # Animation info whilst generating
            label = 'timestep {0}'.format(k)
            print(label)
            return my_plot, self.ax
        anim = FuncAnimation(self.fig, _update, frames=self.nbFrames)
        anim.save(self.filename,
                  dpi=300,
                  writer='imagemagick')


def main():
    # Initialise
    colorPlot = pulsarPlot()
    # Change colour of plot with years
    colorPlot.plotYears()
    # Simple animated spin of the plot
    colorPlot.animateSpin()
    # Opens the gif after saving with local program
    os.system('sxiv -af ' + colorPlot.filename) 


if __name__ == '__main__':
    main()
