import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import normalize

data = np.loadtxt('input_para.csv', delimiter= ',')
y = data[:, 0].astype(np.int)
X = data[:, 1:]
'''for i in range(1, len(y)):
  if y[i]%2 == 0 :
     y[i]=y[i]/2
  if y[i] == 3:
     y[i] = 2'''

for i in range(1,len(y)):
  if y[i]>1:
     y[i]=2
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.2, random_state= 42)
#X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.2, random_state= 1)
# Initialize our classifier

train, test, train_labels, test_labels = train_test_split(X,
                                                          y,
                                                          test_size=0.2,
                                                         random_state=42)
df1 = pd.read_csv('input_para.csv')

df = pd.DataFrame(0, index = df1[:1184].index, columns =['yolo']  )
df['bin'] = pd.Series(y_test, index = df.index )

# Initialize our classifier
gnb = GaussianNB()

# Train our classifier
model = gnb.fit(train, train_labels)

# Make predictions
preds = gnb.predict(test)
df['Logistic'] = pd.Series(gnb.predict(test), index = df.index )

#print(preds)

#print(label_names)

# Evaluate accuracy
cnt1=0
cnt2=0
print(accuracy_score(test_labels, preds))
for i in range(1,len(preds)):
  if preds[i]==1:
     cnt1=cnt1+1
  else:
     cnt2=cnt2+1
print "Total predictions"
print (len(preds))
print "predicted 1"
print (cnt1)
print "predicted 2"
print(cnt2)
#sklearn.svm.libsvm.predict_proba()
df.to_csv('predicted.csv')

