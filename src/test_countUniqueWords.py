# test_countUniqueWords.py
# Purpose:
#   Ensures that the countUniqueWords function properly
#   counts unique words and increases count frequency
#   of identical words.

import unittest
import main

class TestCountUniqueWords(unittest.TestCase):
    # clear the global FOUNDWORDS so tests do not
    # interfere with one another
    def setUp(self):
        main.FOUNDWORDS = {}
        
    def tearDown(self):
        main.FOUNDWORDS = {}
        
    # Given an empty array, check to see
    # if no words are counted.
    def test_countEmptyWords(self):
        words = []
        main.countUniqueWords(words)
        self.assertDictEqual(main.FOUNDWORDS, {})
        self.assertEqual(len(main.FOUNDWORDS), 0)
        self.assertNotEqual(main.FOUNDWORDS, {"word":1})
        
    # Checks to ensure the same identical word's count
    # is incremented by 1.  
    def test_incrementIdenticalWord(self):
        words = []
        main.countUniqueWords(words)
        self.assertDictEqual(main.FOUNDWORDS, {})
        self.assertEqual(len(main.FOUNDWORDS), 0)
        self.assertNotEqual(main.FOUNDWORDS, {"first":1})
        words = ["first"]
        main.countUniqueWords(words)
        self.assertDictEqual(main.FOUNDWORDS, {"first": 1})
        # Give it another word to count and increment by 1
        words = ["first"]
        main.countUniqueWords(words)
        self.assertDictEqual(main.FOUNDWORDS, {"first": 2})
        self.assertNotEqual(main.FOUNDWORDS, {"first":1})
        self.assertNotEqual(main.FOUNDWORDS, {"first": 3})
        words = ["first"]
        main.countUniqueWords(words)
        self.assertDictEqual(main.FOUNDWORDS, {"first": 3})
        self.assertNotEqual(main.FOUNDWORDS, {"first":2})

    # Given an array of the same word, 
    # check to see if count works as intended
    def test_countIdenticalWords(self):
        words = ["word", "word", "word"]
        main.countUniqueWords(words)
        self.assertDictEqual(main.FOUNDWORDS, {'word': 3})
        self.assertNotEqual(main.FOUNDWORDS, {'word': 4})
        self.assertEqual(len(main.FOUNDWORDS), 1)
        self.assertNotEqual(len(main.FOUNDWORDS), 3)

    # Given array of different words, 
    # check to see if counted properly
    def test_countUniqueWords(self):
        words = ["word", "anotherWord", "word", "anotherWord"]
        main.countUniqueWords(words)
        self.assertDictEqual(main.FOUNDWORDS, {'anotherWord': 2, 'word': 2})
        self.assertNotEqual(main.FOUNDWORDS, {'word': 4})
        self.assertEqual(len(main.FOUNDWORDS), 2)
        self.assertNotEqual(main.FOUNDWORDS, {'anotherWord': 2, 'word': 3})
        
    # Given array of the same word with different capitilzations, 
    # only increases the frequency of the same word if capitilzations are 
    # exactly the same.
    def test_countCapitalizedWords(self):
        words = ["word", "Word", "word", "Word", "worD", "Word"]
        main.countUniqueWords(words)
        self.assertDictEqual(main.FOUNDWORDS, {'word': 2, 'Word': 3, "worD": 1})
        self.assertEqual(len(main.FOUNDWORDS), 3)
        self.assertNotEqual(len(main.FOUNDWORDS), 1)
        self.assertNotEqual(main.FOUNDWORDS, {'word': 5})
        
    # Given an array of invalid words (numbers, operators,etc), 
    # check to see if none are counted and FOUNDWORDS is blank.
    def test_countInvalidWords(self):
        words = ["44", "b@dWord", "!", "@", "!test!", "."]
        main.countUniqueWords(words)
        self.assertDictEqual(main.FOUNDWORDS, {})
        self.assertEqual(len(main.FOUNDWORDS), 0)
        self.assertNotEqual(len(main.FOUNDWORDS), 5)
        
if __name__ == '__main__':
    unittest.main()