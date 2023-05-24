import pandas as pd

def get_classes(files):

    #########################################################
    ## INPUT:                                              ##
    ## - files: string containing the name of a .csv table ##
    ##                                                     ##
    ## OUTPUT:                                             ##
    ## - df: dataframe keeping only the 'classes'          ##
    ##        attribute                                    ##
    #########################################################

    df = pd.read_csv(files, delimiter=';')

    df.sort_values(by=['folder'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.drop(columns = ['Unnamed: 0','folder'], inplace=True)



    print(df)
    print(df.columns)

    return df

df = get_classes('files.csv')
print('\n\n',df)

df.to_csv('10classes.csv', index=False)