import pandas as pd
import numpy as np
import json
df = pd.read_csv('binned.csv')
j = len(df.index)

df0 = df[df.bin == 1]
df1 = df[df.bin == 2]
df2 = df[df.bin == 3]
df3 = df[df.bin == 4]


df_sam0 = df0.sample(n=1480)
df_sam1 = df1.sample(n=1480)
df_sam2 = df2.sample(n=1480)
df_sam3 = df3.sample(n=1480)

frames = [df_sam0,df_sam1,df_sam2,df_sam3]
sampled = pd.concat(frames)

df_4 = pd.value_counts(sampled.bin).to_frame().reset_index()
df_4.columns = ['bin','frequency']
print df_4

print len(sampled.index)

out = sampled.to_json(orient='records')[1:-1].replace('},{', '}\n{')
with open('sampled.json', 'w+') as fout:
     fout.write(out)
