import pandas as pd
import numpy as np
import json
df = pd.read_csv('langtest.csv')
for index,row in df.iterrows():
	print (index)
	flag = 0
	fileobj = open('rest_ids.txt');
	for line in fileobj:
		line = line.rstrip('\n')
		print (line)
		print (df.iloc[index,0])
		if (df.iloc[index,0] == line):
			flag = 1
	if (flag == 0):
		df.drop(index, inplace=True)
df.to_csv('out.csv', sep='\t')
