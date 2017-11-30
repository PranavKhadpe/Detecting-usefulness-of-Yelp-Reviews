from datetime import datetime
import pandas as pd
import numpy as np
import json

df = pd.read_csv('/home/josh/python/SNLP/src/truncate_data/epoch_rev.json')
df = df[df.epoch_time < 1483142400.0]
df = df[df.epoch_time > 1419984000.0]
with open('epoch_fil.json', 'w+') as f:
    f.write(out)
