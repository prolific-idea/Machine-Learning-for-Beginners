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
