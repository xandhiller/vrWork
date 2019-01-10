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

dataSource = './src/pulsarCatalogue.csv'


#   plt.show()


def main():
    # Ploting setup
    fig = plt.figure()
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
    ax.set_facecolor((0.0, 0.0, 0.0))
    # Pop up the window with the result
    plt.show()

# TODO
# simple animation with spin


if __name__ == '__main__':
    main()
