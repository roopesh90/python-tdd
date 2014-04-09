import unittest
from Calculator.main import Calculator 

class TddSamplePython(unittest.TestCase):
    def test_calculator_add(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEquals(result, 4)

suite = unittest.TestLoader().loadTestsFromTestCase(TddSamplePython)
unittest.TextTestRunner(verbosity=2).run(suite)

#if __name__ == '__main__':
#    unittest.main()
