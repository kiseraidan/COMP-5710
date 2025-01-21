"""
 Author: Aidan Kiser
 Version: 13 September 2024
"""

import unittest
import source

class TestAddition(unittest.TestCase):
    def testAddition1(self): 
        self.assertEqual(3, source.performAdd(2, 1), "Error in implementation.")

    def testAddition2(self):
        self.assertEqual(101, source.performAdd(100, 1), "Error again!") 

class TestSubtraction(unittest.TestCase):
    def testSub1(self):
        self.assertEqual(5, source.performSub(10, 5), "Error!")
    
    def testSub2(self):
        self.assertEqual(-1, source.performSub(5, 6), "Error in subtraction.")

class TestMultiplication(unittest.TestCase):
    def testMultiply1(self):
        self.assertEqual(25, source.performMutiply(5, 5), "Error in multiplication.")

    def testMultiply2(self):
        self.assertEqual(24, source.performMutiply(6, 4), "Error in multiplication.")

class TestDivision(unittest.TestCase):
    def testDivide1(self):
        self.assertEqual(5, source.performDivide(25, 5), "Error in division.")

    def testDivide2(self):
        self.assertEqual(4, source.performDivide(24, 6), "Error in division.")

    def testDivide3(self):
        self.assertEqual("Error: Division by zero is not allowed.", source.performDivide(100, 0), "Error in division.")


if __name__ == '__main__': 
    unittest.main() 
