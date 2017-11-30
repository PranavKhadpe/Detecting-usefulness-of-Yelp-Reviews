import pandas as pd
import numpy as np
import langid
import json
df = pd.read_csv('/home/josh/python/SNLP/src/truncate_data/small.csv')
df['language'] = pd.Series(0, index=df.index)
j = len(df.index)
for x in range(0, j):
    language = langid.classify(df.iloc[x,6])
    df.iloc[x,9] = language[0]

df = df[df.language == 'en']

out = df.to_json(orient='records')[1:-1].replace('},{', '}\n{')
with open('small_lang.json', 'w') as f:
    f.write(out)
