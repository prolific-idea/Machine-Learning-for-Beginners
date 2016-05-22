import csv
import numpy as np
from sklearn import tree
training_data = [];
training_target = [];
testing_data = [];
testing_target = [];
with open('../Dataset/training.data', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        num = sum(c.isdigit() for c in row[0]) 
        upr = sum(c.isupper() for c in row[0])
        spe = sum( not (c.isalpha()) and  not (c.isdigit()) for c in row[0])
        lgt = len(row[0])
        training_data_item = [num, upr, spe, lgt]
        training_data.append(training_data_item)
        training_target.append(int(row[1]))

with open('../Dataset/testing.data', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        num = sum(c.isdigit() for c in row[0]) 
        upr = sum(c.isupper() for c in row[0])
        spe = sum( not (c.isalpha()) and  not (c.isdigit()) for c in row[0])
        lgt = len(row[0])
        testing_data_item = [num, upr, spe, lgt]
        testing_data.append(testing_data_item)
        testing_target.append(int(row[1]))

#The classifier
clf = tree.DecisionTreeClassifier()
#Training the classifier
clf.fit(training_data, training_target)

testing_expected = testing_target
testing_predicted = clf.predict(testing_data)

diff = map(lambda x,y:x-y, testing_predicted, testing_expected)
print(np.histogram(diff, range(-4, 5)))

hist = {}
for i in range(-4,5):
    hist[i] = 0
    
for i in diff:
    hist[i] += 1
    
for i in range(-4,5):
    print "%2d - %3d" % (i, hist[i])

print sum(map(lambda x: x*x, diff))