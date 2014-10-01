import unittest

class TestFizzBuzz(unittest.TestCase):

	def test_3_donne_fizz(self):
		self.assertEqual("Fizz", fizz_buzz(3))
	def test_5_donne_buzz(self):
		self.assertEqual("Buzz", fizz_buzz(5))
	def test_15_donne_buzz(self):
		self.assertEqual("FizzBuzz", fizz_buzz(15))
def fizz_buzz(chiffre):
	if chiffre % 15 == 0:
		return "FizzBuzz"
	elif chiffre % 3 == 0:
		return "Fizz"
	elif chiffre % 5 == 0:
		return "Buzz"

if __name__ == '__main__':
	unittest.main()
 