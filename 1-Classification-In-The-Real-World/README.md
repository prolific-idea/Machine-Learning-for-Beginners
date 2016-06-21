# Machine Learning - Classification of Text
## Getting Started
You will require the following software:
* [Python](https://www.python.org/)
* [Anaconda (Recommended)](https://www.continuum.io/downloads)
* [SQLite Editor](http://sqlitestudio.pl/)

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
To prepare the data you will have to open a connection to the SQLite database or open the CSV file provided as part of the dataset. If you have python 2.5+ installed then you should already have everything you need to open a new connection to the SQLite database.  Here is a small example of opening the connection and reading the rows:

```python
import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('amazon-fine-foods/database.sqlite')

    cur = con.cursor()
    cur.execute('SELECT * from reviews')

    rows = cur.fetchall()

    for row in rows:
        print row

except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()
```

You can also have a look [here](http://zetcode.com/db/sqlitepythontutorial/) for some more information on reading data from the SQLite database.

Using the goals determined in the previous step begin by extracting the data and transforming it into features. For instance, of your goal is to classify the review score based on keywords (E.g. "Love", "Hate") you will have to read the review text, count the occurrences of the keyword(s) and then store those as part of your features.

Once you have all of the features extracted from the data you can use them to train the classifier. You will also have to think about preparing the data to test the predicted results from the classifier.

## Implement and Experiment
Implement a solution and experiment using a Naive Bayes algorithm.

Scikit-Learn includes various Naive Bayes models for you to use.  You can import the Naive Bayes model of your choice and then train it.  This step is very similar to previous exercise and should be easy to implement.  For some examples you can look [here](http://scikit-learn.org/stable/modules/naive_bayes.html)

There are three types of Naive Bayes models included with the scikit learn library:

1. Gaussian: It is used in classification and it assumes that features follow a normal distribution.
2. Multinomial: It is used for discrete counts. For example, let’s say,  we have a text classification problem. Here we can consider bernoulli trials which is one step further and instead of “word occurring in the document”, we have “count how often word occurs in the document”, you can think of it as “number of times outcome number x_i is observed over the n trials”.
3. Bernoulli: The binomial model is useful if your feature vectors are binary (i.e. zeros and ones). One application would be text classification with ‘bag of words’ model where the 1s & 0s are “word occurs in the document” and “word does not occur in the document” respectively.

Experiment with different features and models and see if you can get the prediction closer to the actual results.
