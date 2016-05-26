from sklearn import tree

f = open("training.data")
lines = f.readlines()
clean_lines = []
labels = []
for line in lines:
    clean_lines.append(line[:line.find('|')])
    labels.append(line[line.find('|')+1:].strip('\n'))
print(labels)
features=[]

for clean_line in clean_lines:
    numCaps = sum(c.isupper() for c in clean_line)
    numSpec = sum(not(c.isalpha()) and not(c.isdigit()) for c in clean_line)
    numNum = sum(c.isdigit() for c in clean_line)
    feature = [numCaps, numSpec, numNum, len(clean_line)]
    features.append(feature)

#The classifier that we're using. A simple decision tree.
clf = tree.DecisionTreeClassifier()
#Training the classifier with the fruit and their labels.
clf = clf.fit(features, labels)

#params = []
f2 = open("testing.data")
test_lines = f2.readlines()

for test_line in test_lines:
    password = test_line[:test_line.find('|')]
    numCaps = sum(c.isupper() for c in password)
    numSpec = sum(not(c.isalpha()) and not(c.isdigit()) for c in password)
    numNum = sum(c.isdigit() for c in password)
    param = [numCaps, numSpec, numNum, len(password)]
    print(test_line.strip('\n')+": "+str(clf.predict([param])[0]))
