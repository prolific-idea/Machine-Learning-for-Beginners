import unittest
from passwords import contains_numeric, contains_upper_case

class TestRegex(unittest.TestCase):
	
	def test_contains_upper_case(self):
		test_input = ['asB']

		for val in test_input: 
			assert contains_upper_case(val) is True

	def test_does_not_contain_numeric(self):
		test_input = ['asd','sadfsfgdgnhg', '$@#sdfsfd', '']

		for val in test_input: 
			assert contains_numeric(val) is False

	def test_does_contain_numeric(self):
		test_input = ['a9', 'a9.0']

		for val in test_input: 
			assert contains_numeric(val) is True


if __name__ == '__main__':
    unittest.main()			