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

