################################################################################
# 
# Author: Alex Hiller
# Year: 2019
# Program Description: Generate plots from `pulsarCatalogue.txt`
# 
################################################################################

import pandas as pd
io = 'pulsarCatalogue.txt'


def main():
    df = pd.read_csv(io) 
    print(df)
    

if __name__ == '__main__':
    main()
