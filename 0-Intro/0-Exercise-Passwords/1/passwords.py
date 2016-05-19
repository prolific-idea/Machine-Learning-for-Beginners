import re
from sklearn import tree

## features:
def is_longer_than_8(str):
	return len(str) > 8

def contains_special_char(str):
	return not str.isalnum()

def contains_upper_case(str):
    return re.search('[A-Z]', str) is not None

def contains_numeric(str):
    return re.search('\d', str) is not None

def get_classifier(classifier):	
	return getattr(tree, classifier)()

def get_features(password):
	"""
	Feel free to play around with 
	the training features - see how 
	adding/removing certain features 
	effects output
	(or add some new ones)
	"""
	return [
		is_longer_than_8(password), 
		contains_special_char(password),
		contains_upper_case(password),
		contains_numeric(password),
	]


def train(lines):
	passwords = []
	labels = []
	features = []

	with open('../Dataset/training.data') as f:
		for line in f.readlines()[0:lines]:
			password, score = line[:-1].split("|")
			passwords.append(password)
			labels.append(score)

			features.append(get_features(password))	

	return (passwords, labels, features)

def test(classifier, passwords, labels, features):

	#The classifier that we're using. A simple decision tree.
	#clf = tree.DecisionTreeClassifier()
	clf = get_classifier(classifier)
	#Training the classifier with the fruit and their labels.
	clf = clf.fit(features, labels)

	correct = 0
	incorrect = 0

	with open('../Dataset/testing.data') as f:
		for line in f.readlines():

			password, score = line[:-1].split("|")
			
			result = clf.predict([get_features(password)])[0]
			iscorrect = result == score
			if iscorrect:
				correct+=1
			else:
				incorrect+=1

	print "Correct: {}" . format (correct)
	print "Incorrect: {}" . format (incorrect)
	print (correct)/250.0

def run():
	"""
	We run the tests with increasingly 
	more of the training data so we can 
	track how the training data effects 
	accuracy
	"""
	classifiers = [
		'DecisionTreeClassifier',
		'ExtraTreeClassifier', 
		'DecisionTreeRegressor', 
		'ExtraTreeRegressor',
	]
	for classifier in classifiers:
		print ("******************")
		print (classifier)
		print ("******************")

		for lines in xrange(1,101,10):

			print "Training with {} lines" . format (lines)
			passwords, labels, features = train(lines)
			test(classifier, passwords, labels, features)
			print "-------------------"


if __name__ == '__main__':
    run()