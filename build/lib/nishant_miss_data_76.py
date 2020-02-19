import pandas as pd
import numpy as np
def imputer(df,argg):
    for col in list(set(df.columns) - set(df._get_numeric_data().columns)):
        frq = df[col].dropna().mode()[0]
        df[col] = df[col].fillna(value=frq)
    for col in df._get_numeric_data().columns:
        if argg==0:
            df[col]=df[col].fillna(value=df[col].mean())
        elif argg==1:
            df[col]=df[col].fillna(value=df[col].median())
        else:
            df[col]=df[col].fillna(value=df[col].mode()[0])
    return df

def filler(df,argg):
    if argg==0:
        nd = df.fillna(method='bfill')
    else:
         nd = df.fillna(method='ffill')   
    return nd
    
def dropvalue(df,along=0):
    nd = df.dropna(axis=along)
    return nd