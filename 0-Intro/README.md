# Machine Learning
## Intro
Traditional Artificial Intelligence (AI) algorithms are designed to solve specific problems. Deep blue was purpose built for playing chess. Game enemy AI are built to attack the player. Most traditional methods of AI approximate a solution for a specific problem.

Machine learning tries to learn more general concepts and work in changing dynamic contexts.

## Types of Learning
There are various ways for learning to happen.

* **Supervised Learning:** The algorithm is given inputs as well as the expected output in a training set. The goal is to learn general rules that map inputs to the correct outputs for future inputs.

* **Unsupervised Learning:** The algorithm is given inputs without expected outputs. The goal is to discover hidden patterns that can be used for future learning.

* **Reinforcement Learning:** The algorithm works with a given input without the expected outputs, and a specific goal that it should aim to achieve. The algorithm should determine if it is closer to it's goal or not.

## Categories Based on Outputs

* **Classification:** Inputs are categorised into two or more groups. Classification generally uses supervised learning.

* **Regression:** Similar to classification, where the outputs are not discrete. There may be categories that were previously unknown.

* **Clustering:** Inputs are categorised into groups, however, the groups are not known. Clustering generally uses unsupervised learning.

## Data
Collecting and preparing data is one of the most important part of machine learning.
The attributes that describe an object are called FEATURES.
The classification of that object is called a LABEL.

* Remove redundant features. E.g. temperature in Fahrenheit, and temperature in Celsius is redundant.

* Remove features that don't add value to classifying the object.

* Ensure no single feature automatically determine the label.

# Getting your hands dirty

## Getting Setup with Python
Ensure that you have the below software installed.

Software you require
* [Python 2.7](https://www.python.org)
* [Anaconda (Recommended)](https://www.continuum.io)

## Getting Setup with R
Software you require
* [R 3.3.0 or R 3.2.5](https://www.r-project.org/)
* [R Studio (Recommended)](https://www.rstudio.com/products/rstudio/download/)

## Hello World
In this Python example we're providing a list of fruit and try to classify them as apples or oranges.
For simplicity, we're using the weight of the fruit and the roughness of it's skin.
If it's rough we're almost sure it's an orange. If it's smooth we're almost sure it's an apple.
```
from sklearn import tree

#The features of fruit. [weight, rough(1) or smooth(0)]
features = [[140, 1],[130, 1],[150, 0],[170, 0]]
#The labels of the fruit in the feature list. Orange(1) or Apple(0) 
labels = [0, 0, 1, 1]

#The classifier that we're using. A simple decision tree.
clf = tree.DecisionTreeClassifier()
#Training the classifier with the fruit and their labels.
clf = clf.fit(features, labels)

#Predicting a new fruit
print clf.predict([[160, 0]])

```

## Iris Flower Classification
This is an expansion of the hello world example with the iris flower dataset.
Here we're trying to predict the type of iris flower based on it's petals and sepals.
This example also demonstrates how to seperate a dataset for training and testing data.
```
from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np

iris = load_iris()
test_idx = [0, 50, 100]

#training data
training_target = np.delete(iris.target, test_idx)
training_data = np.delete(iris.data, test_idx, axis = 0)

#testing data
testing_target = iris.target[test_idx]
testing_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(training_data, training_target)

print testing_target
print clf.predict(testing_data)

#vis code
from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = pydot.graph_from_dot_data(dot_data.getvalue())  
graph.write_svg("iris.svg")

print testing_data[1], testing_target[1]
print iris.feature_names, iris.target_names

```

Or in R

```

data(iris)

# data has not been split into training and testing, we're using the entire set to train.
tree1 <- tree(Species ~ Sepal.Width + Petal.Length + Petal.Width, data = iris)
summary(tree1)

# Visualisation 
# See the decision tree itself
plot(tree1)
text(tree1)

# or the data with the decision boundaries
plot(iris$Petal.Width,iris$Sepal.Width,pch=19,col=as.numeric(iris$Species))
partition.tree(tree1,label="Species",add=TRUE)
legend(1.75,4.5,legend=unique(iris$Species),col=unique(as.numeric(iris$Species)),pch=19)

# References
* [Google Developers YouTube](https://www.youtube.com/playlist?list=PLOU2XLYxmsIIuiBfYad6rFYQU_jL2ryal)
* [Decision trees and forests in R] (http://www.r-bloggers.com/a-brief-tour-of-the-trees-and-forests/)
