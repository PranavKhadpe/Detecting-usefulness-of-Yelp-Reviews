import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('epoch_rev.csv')
print "data loaded"

## Only use the following if you have already run langident.py
df = df[df.review_id != 'P2jAYuFRS1qk87Exw0ypSw']
df.drop('language', axis = 1)
print "dropped language"

# Assuming that anything that hasn't received a vote is unread
df = df[(df.useful + df.funny + df.cool) > 0]
print "dropped unread"
print "\n", len(df.index)

## Only use the following if epoch time is already stored in another column. 
## There is no need to run this if you have already used epoch_remove.py
# dropping all new reviews i.e. starting january 2017
# df = df[df.epoch_time < 1483142400]
# print "dropped new reviews"
# print "\n", len(df.index)

# tabulate distribution of frequency vs number of votes
df_2 = pd.value_counts(df.useful).to_frame().reset_index()
df_2.columns = ['useful votes','frequency']
print df_2

# Defining a new df to store the 'useful' as the only input feature to the clustering algo
df_3 = df['useful']
data = df_3.values.reshape(-1,1)


# Clustering the data
binned = KMeans(n_clusters=6, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1)

binned.fit(data)
predict = binned.predict(data)

# writing the bin of every data point into the dataframe
df_3['bin'] = pd.Series(predict, index=df.index)

# creates a new column in original df to store the bin
df['bin'] = df_3['bin']


# this df is only for testing and counting the freq in each bin
df_4 = pd.value_counts(df.bin).to_frame().reset_index()
df_4.columns = ['bin','frequency']
print df_4


# just prints the first 100 reviews to verify if bin classification has been done properly
print df[:100]

out = df.to_json(orient='records')[1:-1].replace('},{', '}\n{')
with open('binned.json', 'w') as f:
    f.write(out)
