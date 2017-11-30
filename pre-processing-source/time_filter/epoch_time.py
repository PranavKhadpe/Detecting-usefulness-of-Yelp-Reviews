from datetime import datetime
import pandas as pd
import numpy as np
import json

df = pd.read_csv('/home/josh/python/SNLP/src/truncate_data/english_rev.csv')
j = len(df.index)
df['epoch_time'] = pd.Series(0, index=df.index)
with open('epoch_times.txt', 'w+') as file:
	for x in range(0, j):
		utc_time = datetime.strptime(df.iloc[x,2], "%Y-%m-%d")
		epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
		df.iloc[x,10] = epoch_time
		file.write('{}\n'.format(epoch_time))
    	
out = df.to_json(orient='records')[1:-1].replace('},{', '}\n{')
with open('epoch_rev.json', 'w+') as f:
    f.write(out)
