import unittest


class TddSamplePython(unittest.TestCase):
    def add(self, x, y):
        calc = Calculator()
        result = calc.add(2,2)
        assertEqual(result, 4)
    
if __name__ == '__main__':
    unittest.main()