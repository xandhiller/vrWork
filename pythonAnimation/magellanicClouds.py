
################################################################################
# 
# Author: Alex Hiller
# Year: 2019
# Program Description: Small script to determine what the x,y,z of the 
#                       magellanic clouds are.
################################################################################

import pandas as pd

def main():
    df = pd.read_csv('./src/newPulsarCatalogue.csv') 


if __name__ == '__main__':
    main()
