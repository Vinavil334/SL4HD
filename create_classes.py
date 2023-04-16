import pandas as pd

def get_classes(files):

    #########################################################
    ## INPUT:                                              ##
    ## - files: string containing the name of a .csv table ##
    ##                                                     ##
    ## OUTPUT:                                             ##
    ## - df: dataframe keeping only the 'classes'          ##
    #        attribute                                     ##
    #########################################################

    # carica il file csv in un dataframe
    df = pd.read_csv(files, delimiter=';')

    # ordina il dataframe per la seconda colonna
    df.sort_values(by=['folder'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.drop(df.columns[1],axis=1,inplace=True)
    

    df['class']=df['class'].replace([1, 2, 3, 4, 5], 1)
    df['class']=df['class'].replace([6, 7, 8], 2)
    df['class']=df['class'].replace([9, 10], 3)

    print(df)
    print(df.columns)

    return df

df = get_classes('files.csv')
print('\n\n',df)

df.to_csv('classes.csv', index=False)