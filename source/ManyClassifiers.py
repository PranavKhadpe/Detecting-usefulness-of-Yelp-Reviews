'''
Takes as input a CSV File with the bin value in the first column and the remaining features in the next column. Headers have to be removed
Improvements: Instead of feature selection techniques used here, a correlation based feature reduction technique can be used. Read about FCBF.
'''

import numpy as np
import pandas as pd
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
X = data[:, 1:]
y = data[:, 0].astype(np.int)
print X[:3]
print X.shape

# Below are some standard feauture reduction/selection techniques I thought would help but didn't :'
'''
min_max_scaler = MinMaxScaler()
X = min_max_scaler.fit_transform(X)

print X[:3]

X = normalize(X)

## Dimension Reduction
sel = VarianceThreshold(threshold = (0.8*(1-0.8)))
X = sel.fit_transform(X)
print X.shape
'''

# These feature reduction techniques help a bit
clf = ExtraTreesClassifier()
clf = clf.fit(X, y)
model = SelectFromModel(clf, prefit=True)
X = model.transform(X)
print X.shape

X = SelectKBest( chi2, k = 25).fit_transform(X,y)

print X.shape

## Split into test and train data

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.2, random_state= 42)


# This part of the code is to write the test data into another file so that we can check later but requires you to know the dimension after reduction so I have commented out for now.
'''
df1 = pd.read_csv('input_param.csv')
del df1['bin']
print len(X_test)

df = pd.DataFrame(X_test, index = df1[:1184].index, columns = df1.columns )
df['bin'] = pd.Series(y_test, index = df.index )
'''


## SVM One vs one

clf = SVC()
clf.fit(X_train, y_train)

training_accuracy = clf.score(X_train, y_train)
print "Training accuracy = ", training_accuracy
test_accuracy = clf.score(X_test, y_test)
print "Test accuracy = ", test_accuracy

## SVM one vs rest

clf = LinearSVC(random_state = 0)
clf.fit(X_train, y_train)

training_accuracy = clf.score(X_train, y_train)
print "Training accuracy = ", training_accuracy
test_accuracy = clf.score(X_test, y_test)
print "Test accuracy = ", test_accuracy
'''
'''

## Logistic Regression:

clf = LogisticRegression(multi_class = 'ovr')
clf.fit(X_train, y_train)

training_accuracy = clf.score(X_train, y_train)
print "Training accuracy = ", training_accuracy
test_accuracy = clf.score(X_test, y_test)
print "Test accuracy = ", test_accuracy
# df['Logistic'] = pd.Series(clf.predict(X_test), index = df.index )

## Random Forest Classifier

clf = RandomForestClassifier(max_depth = 5)
clf.fit(X_train, y_train)

training_accuracy = clf.score(X_train, y_train)
print "Training accuracy = ", training_accuracy
test_accuracy = clf.score(X_test, y_test)
print "Test accuracy = ", test_accuracy
# df['Random Forest'] = pd.Series(clf.predict(X_test), index = df.index )

#df.to_csv('predicted.csv')


clf = KNeighborsClassifier()
clf.fit(X_train, y_train)

training_accuracy = clf.score(X_train, y_train)
print "Training accuracy = ", training_accuracy
test_accuracy = clf.score(X_test, y_test)
print "Test accuracy = ", test_accuracy
