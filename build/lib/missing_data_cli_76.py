#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
from nishant_miss_data_76 import dropvalue,filler,imputer

def main():
	arguments = sys.argv[1:]
	assert len(arguments) >= 2 and len(arguments) <= 4, "Wrong number of arguments provided"

	filename_in = arguments[0]
	filename_out = arguments[1]
	assert filename_in, "Input CSV filename must be provided"
	assert filename_out, "Input CSV filename must be provided"
	df=pd.read_csv(filename_in)
	if len(arguments) == 2:
	        output = dropvalue(df)
	        
	elif len(arguments) == 4:
	    req_arg = int(arguments[3])
	    if arguments[2] == 'DROP':
	        output = dropvalue(df,req_arg)
	    elif arguments[2] == 'FILL':
	        output = filler(df,req_arg)
	    elif arguments[2] == 'IMPUTE':
	        output = imputer(df,req_arg)
	    else:
	        print('Invalid arguments provided')
	else:
	    print('Invalid number of arguments provided - need to be either 2 or exactly 4')

	output.to_csv(filename_out,index=False)