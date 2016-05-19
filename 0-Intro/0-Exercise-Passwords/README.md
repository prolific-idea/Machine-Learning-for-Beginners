# Password Strength Machine Learning
Provided is a dataset of passwords. This can be used to extract properties to determine the strength of the password.

## Rules for Password Strength
These are the rules that we will use for password strength. Passwords have a strength between 0 and 4.
Lets assign points to passwords.
* A password with a character length of 8 or more gets 1 point.
* A password containing a special character, an uppercase alphabet character, and a numeric character gets an additional 3 points.
* A password containing an uppercase alphabet character, and a numeric character gets an additional 1 points.
* A password containing a special character, and a numeric character gets an additional 2 points.
* A password containing a special character, and an uppercase alphabet character gets an additional 2 points.
* A password that does not meet any of these requirements gets a 0 points.

## The Dataset
The following data sets are provided:
* **Training:** A training dataset for training your machine learning algorithm.
* **Testing:** A training dataset for testing your machine learning algorithm.

## Preparing the Data
The passwords as they exist have no meaning to a machine learning algorithm.
You will need to extract properties of the password that can be used.
Example: Number of special character.
