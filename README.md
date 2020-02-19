# Handling Missing Data 

```
This package has been created based on Project 3 of course UCS633(DATA ANALYSIS AND VISUALISATION ) Thapar University, Patiala
Nishant Goel  
COE17
Roll number: 101703376
```

Output is a DataFrame with all **NaN** removal 

## Installation
`pip install nishant_missing_data_76`

*Recommended - test it out in a virtual environment.* 

## Upgrade
`pip install nishant_missing_data_76 --upgrade`

## To use via command line
`missing_data_cli_76 in.csv out.csv`

Drop rows with NaN
`missing_data_cli_76 in.csv out.csv DROP 0` 

Drop columns with NaN
`missing_data_cli_76 in.csv out.csv DROP 1`

Forward filling
`missing_data_cli_76 in.csv out.csv FILL 0`

Backward filling
`missing_data_cli_76 in.csv out.csv FILL 1`

Imputing with mean
`missing_data_cli_76 in.csv out.csv IMPUTE 0`

Imputing with median
`missing_data_cli_76 in.csv out.csv IMPUTE 1`

Imputing with mode
`missing_data_cli_76 in.csv out.csv IMPUTE 2`


## To use in .py script
```
from nishant_miss_data_76 import dropvalue,filler,imputer
df=pd.read_csv('file1.csv')
```
```
nd=dropvalue(df,0)
```
```
nd=dropvalue(df,1)
```
```
nd=imputer(df,0)//mean
```
```
nd=imputer(df,1)//median
```
```
nd=imputer(df,2)//mode
```
```
nd=filler(df,along=0)
```
```
nd=filler(df,along=1)
```