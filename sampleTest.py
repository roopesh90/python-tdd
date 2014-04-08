import unittest
from Calculator.main import Calculator 

class TddSamplePython(unittest.TestCase):
    def test_calculator_add(self):
        calc = Calculator()
        result = calc.add(2,2)
        assertEqual(result, 4)
    
if __name__ == '__main__':
    unittest.main()