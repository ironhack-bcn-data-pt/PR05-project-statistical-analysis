from functools import reduce
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns


def strip_col(df):
    [df.rename({i: i.strip() for i in df.columns})]

def dropna_row(df,col_names):
    col_list = [i for i in col_names]
    for i in col_list:
        df.dropna(subset=[i],inplace=True)

def changetype_col(df,col_names,typ):
    col_list = [i for i in col_names]
    for i in col_list:
        df[i] = df[i].astype(typ)
        
def to_num(df):
    col_list = [i for i in df.columns]
    for i in col_list:
        try:
            df[i] = pd.to_numeric(df[i])
        except:
            print(f'{i} not numeric')

def clear_outliers(df,column):
    from scipy.stats import zscore
    print(f'original number of rows: {len(df)}')
    df['zscore'] = zscore(df[column])
    df['is_outlier'] = df['zscore'].apply(lambda x: x <= -1.96 or x >= 1.96)
    df = df[df["is_outlier"] == False]
    #df.drop('zscore',inplace=True)
    #df.drop('is_outlier',inplace=True)
    print(f'processed number of rows: {len(df)}')

