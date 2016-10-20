# Machine Learning - Neural Networks
## Getting Started
You will require the following software:
* [Python](https://www.python.org/)
* [Anaconda (Recommended)](https://www.continuum.io/downloads)
* [SciKit-Learn](http://scikit-learn.org/stable/install.html)

## Interesting Links
* [Tensor Flow](https://www.tensorflow.org/)
* [Tensor Flow Playground](http://playground.tensorflow.org/)
* [Fast Text](https://github.com/facebookresearch/fastText)
* [Google AI XPrize](http://ai.xprize.org/)
* [List of popular github projects related to deep learning](https://github.com/aymericdamien/TopDeepLearning)
* [Something cool to watch](https://www.youtube.com/watch?v=qv6UVOQ0F44)


## Dataset: Wine Quality

### We are reusing the same dataset as the last meetup, but you can use the password dataset or any other dataset you like.

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
Create a classification Neural Network using your language and library of choice.  Keep in mind that training a Neural Network can take a long time and might require multiple passes of the same data due to the small error adjustments being made with every pass.

## Libraries and languages

### SciKit Learn

Scikit learn is a python library with a whole range of different machine learning algorithms.  For Nueral Networks you can use the [Multi-Layer Perceptron](http://scikit-learn.org/dev/modules/neural_networks_supervised.html#classification)

### Java

Java developers can make use of [deeplearning4j](http://deeplearning4j.org/).  It is not as extensive as Scikit-Learn but it can be used for deep learning and Neural Networks.

### .Net

.Net developers can make use of [The Accord Framework](http://accord-framework.net/).  It is not as extensive as Scikit-Learn but has most of the libraries available and is quite easy to use.

### R

R can also be used for Neural Networks and an explanation of how to accomplish it you can have a look at [this blog post](https://www.r-bloggers.com/fitting-a-neural-network-in-r-neuralnet-package/)
