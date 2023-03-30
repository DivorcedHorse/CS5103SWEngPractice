# test_validateWord.py
# Purpose:
#   Ensures that given different words, validateWord will only
#   return True if a word meets the correct requirements.

import unittest
import main

class TestValidateWord(unittest.TestCase):
    # clear the global FOUNDWORDS so tests do not
    # interfere with one another
    def setUp(self):
        main.TOTAL_CHARACTER_COUNTER = 0
        main.TOTAL_LINE_COUNTER = 0
        main.FOUNDWORDS = {}
    def tearDown(self):
        main.TOTAL_CHARACTER_COUNTER = 0
        main.FOUNDWORDS = {}
        main.TOTAL_LINE_COUNTER = 0
        
    # Given a number, validateWord 
    # returns false as not a valid word
    def test_invalidNumbers(self):
        num1 = "1"
        num2 = "123"
        num3 = ".05"
        num4 = "0x12"
        num5 = "105"
        self.assertEqual(main.validateWord(num1), False)
        self.assertEqual(main.validateWord(num2), False)
        self.assertEqual(main.validateWord(num3), False)
        self.assertEqual(main.validateWord(num4), False)
        self.assertEqual(main.validateWord(num5), False)
        self.assertNotEqual(main.validateWord(num5), True)
    
    # Given an operator/symbol, validateWord 
    # should return false as not a valid word
    def test_invalidOperators(self):
        op1 = "!"
        op2 = "?"
        op3 = "*"
        op4 = "."
        op5 = "@"
        self.assertEqual(main.validateWord(op1), False)
        self.assertEqual(main.validateWord(op2), False)
        self.assertEqual(main.validateWord(op3), False)
        self.assertEqual(main.validateWord(op4), False)
        self.assertEqual(main.validateWord(op5), False)
        self.assertNotEqual(main.validateWord(op5), True)

    # Given a word with only valid characters, validateWord 
    # should return True.
    def test_validWord(self):
        validWord1 = "Good"
        validWord2 = "GOOD"
        validWord3 = "exquisite"
        validWord4 = "a"
        validWord5 = "awesome"
        self.assertEqual(main.validateWord(validWord1), True)
        self.assertEqual(main.validateWord(validWord2), True)
        self.assertEqual(main.validateWord(validWord3), True)
        self.assertEqual(main.validateWord(validWord4), True)
        self.assertEqual(main.validateWord(validWord5), True)
        self.assertNotEqual(main.validateWord(validWord5), False)
    
    # Given a word with only valid characters and an acceptable
    # operator/symbol at the end of the word (!, ?, ., ,, ;),
    # validateWord should return True
    def test_validWordWithSymbol(self):
        validWord1 = "Good!"
        validWord2 = "GOOD?"
        validWord3 = "exquisite."
        validWord4 = "a,"
        validWord5 = "awesome;"
        validWord6 = "another:"
        self.assertEqual(main.validateWord(validWord1), True)
        self.assertEqual(main.validateWord(validWord2), True)
        self.assertEqual(main.validateWord(validWord3), True)
        self.assertEqual(main.validateWord(validWord4), True)
        self.assertEqual(main.validateWord(validWord5), True)
        self.assertEqual(main.validateWord(validWord6), True)
        self.assertNotEqual(main.validateWord(validWord6), False)
        
    # Given a word with only valid characters but with many symbols
    # at the end, validateword should return false.
    def test_InvalidWordWithManySymbol(self):
        invalidWord1 = "Good!!"
        invalidWord2 = "GOOD??"
        invalidWord3 = "exquisite.."
        invalidWord4 = "a,,"
        invalidWord5 = "awesome;;"
        invalidWord6 = "!badtoo"
        self.assertEqual(main.validateWord(invalidWord1), False)
        self.assertEqual(main.validateWord(invalidWord2), False)
        self.assertEqual(main.validateWord(invalidWord3), False)
        self.assertEqual(main.validateWord(invalidWord4), False)
        self.assertEqual(main.validateWord(invalidWord5), False)
        self.assertEqual(main.validateWord(invalidWord6), False)
        self.assertNotEqual(main.validateWord(invalidWord5), True)

if __name__ == '__main__':
    unittest.main()