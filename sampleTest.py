import unittest
from Calculator.main import Calculator 

class TddSamplePython(unittest.TestCase):
	def test_calculator_add(self):
		calc = Calculator()
		result = calc.add(2,2)
		self.assertEquals(result, 4)

	@unittest.skip("demo test skipping")
	def test_calculator_subtract(self):
		calc = Calculator()
		result = calc.subtract(2,2)
		self.assertEquals(result, 0)

suite = unittest.TestLoader().loadTestsFromTestCase(TddSamplePython)
unittest.TextTestRunner(verbosity=2).run(suite)

#if __name__ == '__main__':
#    unittest.main()
