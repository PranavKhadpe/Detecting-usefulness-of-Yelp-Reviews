import pandas as pd
import numpy as np

df = pd.read_csv('binned.csv')
print "data loaded"

j = len(df.index)
for x in range(0,j):
    ubin = df.iloc[x,0]
    if ubin == 0:
        ubin = 1
    elif ubin == 4:
        ubin = 2
    elif ubin == 5:
        ubin = 3
    else:
        ubin =4
    df.iloc[x,0] = ubin

df_4 = pd.value_counts(df.bin).to_frame().reset_index()
df_4.columns = ['bin','frequency']
print df_4

out = df.to_json(orient='records')[1:-1].replace('},{', '}\n{')
with open('binned.json', 'w') as f:
    f.write(out)
