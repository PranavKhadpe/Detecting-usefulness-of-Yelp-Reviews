# Detecting-usefulness-of-Yelp-Reviews
Term Project for SNLP course Autumn 2017

# Dataset
The data used is the publicly released data by Yelp as part of the Yelp Dataset challenge. The data can be obtained [here](https://www.yelp.com/dataset/challenge).

# Instructions

Each folder has it's own comprehensive README file. Follow these steps to implement our approach.

* Download the data from the yelp website. If you want to jump directly to testing, you can use 'clean_sample.json' in our 'data' folder.
* Go to the pre-processing folder and follow the instructions given in the README file in that folder.
* Extract LIWC features for the text (Note: LIWC features are proprietary. The code for the feature extraction is hence not included). If you don't have the license you can use the features we extracted, found in the 'data' folder in a text file.
* Use the 'Many_Classifiers.py' file in the 'source' folder to run different models and see their accuracies. Also run 'Observing_dist.py' to see where misclassification occurs. Have a look at the README file there as well.

You can read the project report (report.pdf) to have a clear idea of our approach and our results.

