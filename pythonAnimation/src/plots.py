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
        self.dataSource = './src/newPulsarCatalogue.csv'
        self.filename   = 'run.gif'
        self.df         = pd.read_csv(self.dataSource) 
        self.x          = self.df['XX']
        self.y          = self.df['YY']
        self.z          = self.df['ZZ']
        self.date       = self.df['DISC_DATE']
#       self.luminosity = self.getLuminosity()
        self.sun        = [0, 8.5, 0]
        self.years      = self.getYears()
        self.fig        = plt.figure(facecolor='k', edgecolor='k')
        self.ax         = self.fig.add_subplot(111, projection='3d')
        self.plotOurSun = True
        self.show       = True
        self.magellanic = True
        self.cloudOne   = [-7.69,-19.0,-31]
        self.cloudTwo   = [-41,25,-34]
        self.datapSize = 0.5
        self.ax.set_axis_off()
        self.ax.set_facecolor((0.0, 0.0, 0.0))
        self.year_increment = 20
        self.nbFrames = np.arange(0, 10)
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

        # Plotting Luminosity proportional to transparency
#       def getLuminosity(self):
#           bottom  = min(self.df['R_LUM'])
#           top     = max(self.df['R_LUM'])
#           lumClean = []
#           for i,el in enumerate(self.df['R_LUM']):
#               # If no value available, assume half max brightness
#               if el == np.nan:
#                   lumClean.append(0.5)
#               else:
#                   newVal = lumRaw/top # Scale between 0 and 1
#                   lumClean.append(newVal)
#           df = self.df[
#           return lumClean

    # Plot (with colour) the years of discovery of pulsars
    def plotYears(self):
        # Arithmetic for generating year intervals
        bottom = min(self.years)
        upper = min(self.years) + self.year_increment 
        top = max(self.years)
        intervals = ceil(len(self.years)/self.year_increment)
        # Plot each series of years 
        for interval in range(intervals):
            _x,_y,_z, _luminosity = [],[],[],[]
            # Truncate year values
            _df = self.df[self.df.DISC_DATE <= upper]
            _df = _df[_df.DISC_DATE >= bottom]
            # Format df columns for plotting
            _x          = list(_df['XX'].values)
            _y          = list(_df['YY'].values)
            _z          = list(_df['ZZ'].values)
            _luminosity = list(_df['R_LUM'].values)
            # Generate label for legend
            _label = str(bottom) + ' - ' + str(upper)         
            # Actually plot it.
            self.ax.scatter(_x, _y, _z, label=_label, s=self.datapSize, 
                            alpha=0.3)  
            # Update year interval
            bottom += self.year_increment  
            if upper + self.year_increment < top:
                upper += self.year_increment 
            else:
                upper = top
        if self.plotOurSun == True:
            self.ax.scatter(self.sun[0], self.sun[1], self.sun[2], 
                           s=300, marker='o', zorder=2, edgecolors='r', 
                           alpha=0.5, c='orange', linewidths=0.5, 
                           label='You are here.')
        if self.magellanic == True:
            c1 = self.cloudOne
            c2 = self.cloudTwo
            sun = self.sun
            x1 = [sun[0], c1[0]]
            x2 = [sun[0], c2[0]]
            y1 = [sun[1], c1[1]]
            y2 = [sun[1], c2[1]]
            z1 = [sun[2], c1[2]]
            z2 = [sun[2], c2[2]]
            # cloud 1
            self.ax.plot(x1,y1,z1, color='white', alpha=0.3)
            # cloud 2 
            self.ax.plot(x2,y2,z2, color='white', alpha=0.3)
            # self.ax.plot(
        # Show the legend
        self.ax.legend()
        plt.show()

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
    #colorPlot.animateSpin()
    # Opens the gif after saving with local program
    os.system('sxiv -af ' + colorPlot.filename) 


if __name__ == '__main__':
    main()
