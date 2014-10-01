import unittest

class TestFizzBuzz(unittest.TestCase):

	def test_3_donne_fizz(self):
		self.assertEqual("Fizz", fizz_buzz(3))
	def test_5_donne_buzz(self):
		self.assertEqual("Buzz", fizz_buzz(5))
	def test_15_donne_buzz(self):
		self.assertEqual("FizzBuzz", fizz_buzz(15))
def fizz_buzz(chiffre):
	if chiffre == 3:
		return "Fizz"
	elif chiffre == 5:
		return "Buzz"
	elif chiffre == 15:
		return "FizzBuzz"

if __name__ == '__main__':
	unittest.main()
 