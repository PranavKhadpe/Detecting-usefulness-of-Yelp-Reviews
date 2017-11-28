import pandas as pd
import numpy as np

df = pd.read_csv('sampled.csv')
del df['language']
del df['funny']
del df['useful']
del df['cool']
del df['user_id']
del df['review_id']
del df['date']
del df['business_id']
del df['epoch_time']

out = df.to_json(orient='records')[1:-1].replace('},{', '}\n{')
with open('clean_sample.json', 'w') as f:
    f.write(out)
