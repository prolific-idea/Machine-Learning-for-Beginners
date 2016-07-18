# Machine Learning - Classification of Wine Quality
## Getting Started
You will require the following software:
* [Python](https://www.python.org/)
* [Anaconda (Recommended)](https://www.continuum.io/downloads)

## Dataset: Wine Quality
This dataset has been obtained from [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Wine+Quality).
For sources and citations please visit that page.

The dataset consists of the following features:
* fixed acidity
* volatile acidity
* citric acid
* residual sugar
* chlorides
* free sulfur dioxide
* total sulfur dioxide
* density
* pH
* sulphates
* alcohol

The dataset contains a column `quality` with a score between 0 and 10 that can be used as the target.

## Explore the Dataset
The Wine Quality dataset is an interesting dataset to explore supervised learning using linear regression.

It is important to note that the quality score has been provided using sensory data so it might not reflect real world results in this scenario.  Additionally there is no data about grape types, wine brand, wine selling price, etc. for privacy and logistic reasons.  The data available however will be enough for us to learn the basic understanding of regression classification.  Also keep in mind that there are much more normal wines than excellent or poor ones so you will have to account for outliers.

Not all of the features would contribute to the quality wine, further more some features might carry more weight than others so plan for this when you writing the algorithm.

## Determine Goals

The obvious goal here is to determine the quality of a wine based on a input feature.

You can however explore the data a bit more and see if there are connections between some of the various features.  Regression is different to classification in that values can be predicted, use this knowledge to see if other features can be predicted.

## Prepare the Data
To prepare the data you will have to open the CSV file provided as part of the dataset.

```python
import csv

with open('winequality-red.csv', 'rb') as csvfile:
  winereader = csv.reader(csvfile, delimiter=';', quotechar='"')
  for row in spamreader:
    print row
```

More information about reading CSV files in python can be found [here](https://docs.python.org/2/library/csv.html).

Remember that you will have to separate the data into training and testing data sets.  For example you can use the first 80% or the rows to train the algorithm and the remaining 20% to test it.

## Implement and Experiment
Implement a solution and experiment using a Regression algorithm.

Scikit-Learn includes various regression models for you to use.  You can import the regression model of your choice and then train it.

The easiest would be to use a Linear Regression model. For an example of how to use it you can have a look [here](http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html).
Linear regressing takes a single feature for its X axis, and uses the target as the Y axis.  So for example, you can have `fixed acidity` as your feature (X) and then `quality` as target (Y), using that to train the algorithm you will then be able to predict wine quality based on the `fixed acidity feature`

## Other libraries and languages

For the more adventurous types you can also make use of other libraries.  We have identified the following libraries for Java and .Net that you can use to perform similar tasks.  We have not tested these libraries yet though so they might not work as expected and we might not be able to assist you if you get stuck, but we will help where we can.

### Java

Java developers can make use of [deeplearning4j](http://deeplearning4j.org/).  It is not as extensive as Scikit-Learn but you can accomplish some of the tasks here using this library.  `deeplearning4j` uses neural networks for it's regression tasks and for some examples on how this is accomplished you can have a look [here](http://deeplearning4j.org/linear-regression).

### .Net

.Net developers can make use of [The Accord Framework](http://accord-framework.net/).  It is not as extensive as Scikit-Learn but has most of the libraries available and is quite easy to use.  For an example on using it for this exercise you can have a look [here](http://accord-framework.net/docs/html/T_Accord_Statistics_Models_Regression_Linear_SimpleLinearRegression.htm)
