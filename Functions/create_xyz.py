import numpy as np
import pandas as pd
import glob

def create_list(path):

    #########################################################
    ## INPUT:                                              ##
    ## - path: name of a folder containing multiple .csv   ##
    ##         tables                                      ##
    ## OUTPUT:                                             ##
    ## - ls: list containing all the .csv tables           ##
    #########################################################

    all_files = glob.glob(path + "*.csv")
    ls = []

    for filename in all_files:
        df = pd.read_csv(filename, names = ["x","y","z","t"])
        ls.append(df)

    return ls

def get_polynomials(ls,k):

    #########################################################
    ## INPUT:                                              ##
    ## - ls: list of .csv tables each made of measurements ##
    ##       along space axes x, y, z over time t          ##
    ## - k: degree of the polynomial fit                   ##
    ##                                                     ##
    ## OUTPUT:                                             ##
    ## - df: dataframe with original tables as rows and    ##
    ##       coefficients of the polynomial fit along x, y ##
    ##       and z as columns                              ##
    #########################################################

    # Create columns of the output dataset
    columns = []
    for prefix in ['x', 'y', 'z']:
        for i in range(0, k+1):
            columns.append(f"{prefix}_{i}")
    df = pd.DataFrame(columns=columns)

    # Loop over all the .csv tables
    for i in np.arange(len(ls)): #da cambiare con len(ls)

        # Get values from every table
        x = np.asarray(ls[i].x)
        y = np.asarray(ls[i].y)
        z = np.asarray(ls[i].z)
        t = np.asarray(ls[i].t)

        # Get coefficients of the polynomial fit of order k of x, y, z
        coef_x = np.polyfit(t,x,deg=k,full=False)
        coef_y = np.polyfit(t,y,deg=k,full=False)
        coef_z = np.polyfit(t,z,deg=k,full=False)
        
        # Add coefficients to the final dataset
        row = []
        for j in np.arange(k+1):
            row.append(coef_x[j])
        for j in np.arange(k+1):
            row.append(coef_y[j])
        for j in np.arange(k+1):
            row.append(coef_z[j])
        df.loc[i] = row

    return df.set_index(pd.Index(range(1, len(df)+1)))

path = "C:/Users/markh/Desktop/Università/Healthcare Data/Projects-20230408/Archivio/IFMBE Scientific Challenge/Train2/"
df = get_polynomials(create_list(path), 5)

df.to_csv('xyz.csv', index=False)