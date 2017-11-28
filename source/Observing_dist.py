'''
This code takes as input predicted.csv and tells you how many were predicted correctly and off by 1,2 so on for both RF and Logistic as these outperform others. However to create predicted.csv see commented part in ManyClassifiers.py
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('predicted.csv')

# df['logistic_dist'] = df.Logistic - df.bin
df['random_dist'] = df.Random - df.bin

# df['logistic_dist'] = df['logistic_dist'].abs()
df['random_dist'] = df['random_dist'].abs()

# df_4 = pd.value_counts(df.logistic_dist).to_frame().reset_index()
# df_4.columns = ['logistic_dist','frequency']
# print df_4

df_5 = pd.value_counts(df.random_dist).to_frame().reset_index()
df_5.columns = ['random_dist','frequency']
print df_5
