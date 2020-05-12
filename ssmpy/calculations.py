import numpy as np


def calculate_information_content_intrinsic(df, max_freq):
    '''
    Calculates the information content
    of a dataframe of entries
    :param df: pandas DataFrame
    :param max_freq: maximum frequency in the ontology
    :return: df with extra column 'IC'
    '''

    df['freq_'] = df.desc + 1
    df['IC'] = -(np.log(df.freq_ / max_freq))

    return df
