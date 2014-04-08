import unittest

class TddSamplePython(unittest.TestCase):
    calc = Calculator()
    result = calc.add(2,2)
    assertEquals(result, 4)