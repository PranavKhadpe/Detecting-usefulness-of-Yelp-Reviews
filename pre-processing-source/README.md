# Pre-processing of the data

These codes were used to filter out data based on four criterion:
1) Time the review was written (only those written between 2015 and 2017 were kept)
2) Only reviews of restaurants were kept
3) Reviews that had 0 useful, funny and cool votes were removed to ensure all reviews were seen atleast once
4) Non-English reviews were removed

## lang_filter 

Contains a python code to remove non-English reviews using the langid classifier

## restaurant_filter
Only keeps reviews written for restaurants. This is done by comparing the business ids of the reviews with the business ids of restaurants found in the business.json file of the yelp dataset.

## time_filter

Removes reviews written before 2015 and after 2017 based on epoch times.

## How to use

The first three folders are only so that the data can be seen and analysed at each filtering step. The filtering code is compiled into 1 file (secondfilt.py). Fields that we do not use are removed by throw_out_unnec.py, since we are only concerned about the text of the review and number of useful votes it received after the filtering is done.

second_filt.py also contains k means clustering for the useful votes. k means does not sort the bins it generates according to the votes. We do that manually in changingbin.py

At every step, whenever there is a need to convert from json format to csv, we use json_to_csv.py

All file addresses need to be modified according to where you store your files in your local system.
So the order in which this must be deployed is:
* Run secondfilt.py
* Run throw_out_unnec.py
* Run changingbin.py

Plus you can see the filtered output at each stage using the first three folders' codes.
