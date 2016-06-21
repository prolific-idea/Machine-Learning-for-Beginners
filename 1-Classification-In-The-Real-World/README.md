# Machine Learning - Classification of Text
## Getting Started
You will require the following software:
* [Python](https://www.python.org/)
* [Anaconda (Recommended)](https://www.continuum.io/downloads)
* [SQLite Editor]()

## Dataset: Amazon Fine Food Reviews
This dataset is from [kaggle.com](https://www.kaggle.com/snap/amazon-fine-food-reviews). The dataset consists of 568,454 food reviews Amazon users left up to October 2012.

The dataset consists of the following features:
* Id
* ProductId - unique identifier for the product
* UserId - unqiue identifier for the user
* ProfileName
* HelpfulnessNumerator - number of users who found the review helpful
* HelpfulnessDenominator - number of users who indicated whether they found the review helpful
* Score - rating between 1 and 5
* Time - timestamp for the review
* Summary - brief summary of the review
* Text - text of the review

## Explore the Dataset
The Amazon Fine Food Review dataset is an interesting dataset to explore supervised classification on text data. 

Using the SQLite database, it's possible to explore the data with your own queries.

These are some examples of queries that may produce some interesting results:
* The number of reviews that scored x vs total number of reviews.
* The number of reviews that scored x and contain key words (E.g. "love", "like", "enjoy", "hate", "terrible").
* The number of reviews that are scored x vs how helpful the review was to other users.

## Determine Goals
Various classification goals can be explored using this dataset.

By exploring the data, try and create goals for the classifier.

* A possible goal is determining the score of a review based on the text in the review. This would imply that there is a relationship between key words (possibly the context of the words), and a review score. This relationship is not a given and will need to be tested.

## Prepare the Data
Tips for prep

## Implement and Experiment
Use Naive Bayes
