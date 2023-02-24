# test_checkFiles.py
# Purpose:
#   Ensures passing in files will read and count words properly.

import unittest
import main
import os
import io
import sys

# Testdata files
testCase003 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase003.txt')
testCase004 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase004.txt')
testCase005 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase005.txt')
testCase006 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase006.txt')

class TestCheckFiles(unittest.TestCase):
    # clear the global FOUNDWORDS so tests do not
    # interfere with one another
    def setUp(self):
        main.FOUNDWORDS = {}
        
    # Given an empty file, no words should be counted.
    def test_checkValidSingleEmptyFile(self):
        main.readFile(testCase003)
        self.assertEqual(main.FOUNDWORDS, {})
        self.assertEqual(len(main.FOUNDWORDS), 0)

    # Given a simple text file, check to see if file is
    # properly read and words are counted.
    def test_validFileGiven(self):
        main.readFile(testCase004)
        self.assertNotEqual(main.FOUNDWORDS, {})
        self.assertEqual(main.FOUNDWORDS, {'test':3, 'there':1, 
            'are':1, 'many':1, 'unique':1, 'words':1, 'in':1, 'here':1})
        self.assertEqual(len(main.FOUNDWORDS), 8)
        self.assertNotEqual(len(main.FOUNDWORDS), 0)
        
    # Given a simple text file, check to see if file is
    # properly read and words are counted.
    def test_singleUniqueWordFrequency(self):
        main.readFile(testCase005)
        self.assertNotEqual(main.FOUNDWORDS, {})
        self.assertEqual(main.FOUNDWORDS, {'Unique':10})
        self.assertNotEqual(main.FOUNDWORDS, {'Unique':1})
        self.assertNotEqual(len(main.FOUNDWORDS), 0)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        main.printWords()
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        output = output.rstrip()
        expectedString = "\"Unique\" has a word count of 10"
        self.assertEqual(expectedString, output)

    # Given an actual text file, check to see if file is
    # properly read and words are counted with spaces, tabs, and
    # newlines
    def test_fileWithManySeparators(self):
        main.readFile(testCase006)
        self.assertNotEqual(main.FOUNDWORDS, {})
        self.assertNotEqual(main.FOUNDWORDS, {'words':1, 'with':1, 
            'spaces':1, 'tabs':1, 'and':1, 'newlines':1})
        self.assertEqual(main.FOUNDWORDS, {'words':1, 'with':1, 
            'spaces':1, 'tabs':3, 'and':3, 'newlines':2})
        self.assertEqual(len(main.FOUNDWORDS), 6)
        self.assertNotEqual(len(main.FOUNDWORDS), 0)

if __name__ == '__main__':
    unittest.main()