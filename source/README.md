# Source code

These files are used for running the classifiers and observing the results

Please note that LIWC features are proprietary. We have hence not included the code for their extraction. You need to obtain the license and extract the features for the reviews, and then store them in a file called 'input_par.csv' in the same order as the reviews.

## ManyClassifiers.py

Once you have the features stored, run this file to train SVM one vs one, SVM one vs all, maxent, K nearest neighbours, and random forest models and observe their accuracies. The results are stored in 'predicted.csv' if you follow the instructions in the documentation of the code.

## Observing_dist.py

This code takes as input predicted.csv and tells you how many were predicted correctly and off by 1,2 so on. This enables you to have a clearer idea of where the misclassification is occuring, and if the results are actually useful (which they turn out to be!)


