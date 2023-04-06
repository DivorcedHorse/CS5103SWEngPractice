# test_replaceWord.py
# Purpose:
#   Validates that all functions relating to replacing a word
#   for a specified document works as intended.

import unittest
import main
import os
import io
import sys
from unittest.mock import patch

testCase004 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase004.txt')
testCase011 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase011.txt')
testCase012 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase012.txt')

class TestLineCount(unittest.TestCase):
    # clear the line counter and words before
    # each given test.
    def setUp(self):
        main.TOTAL_CHARACTER_COUNTER = 0
        main.TOTAL_LINE_COUNTER = 0
        main.FOUNDWORDS = {}
    def tearDown(self):
        main.TOTAL_CHARACTER_COUNTER = 0
        main.FOUNDWORDS = {}
        main.TOTAL_LINE_COUNTER = 0
        
        
    # Given a file with no words in the FOUNDWORDS dictionary,
    # ensures that validWordsCheck returns false so that 
    # user will not be prompted to replace a word
    def test_existsValidWords(self):
        self.assertEqual(False, main.validWordsCheck())
        
        # give it valid words to see if returns true
        main.FOUNDWORDS["true"] = 1
        self.assertEqual(True, main.validWordsCheck())
        self.assertNotEqual(False, main.validWordsCheck())
        
    # check to see if given a valid file if any valid words
    # are found and if FOUNDWORDS dictionary is populated
    def test_fileWithInvalidWords(self):
        main.readFile(testCase011)
        self.assertEqual(False, main.validWordsCheck())
        
        # check if found words return true
        main.readFile(testCase004)
        self.assertEqual(True, main.validWordsCheck())

    # Given a word, checks to see if it exists in the 
    # FOUNDWORDS.  If it does, return true, else returns false.
    def test_findValidWord(self):
        main.FOUNDWORDS["exist"] = 1
        main.FOUNDWORDS["good"] = 10
        
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        self.assertEqual(True, main.findWordInFile("exist"))
        self.assertEqual(True, main.findWordInFile("good"))
        self.assertEqual(False, main.findWordInFile("bad"))
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        output = output.rstrip()

    # Given a word that does not exist in FOUNDWORDS, ensure
    # error message is printed as well
    def test_findInvalidWordPrint(self):
        main.FOUNDWORDS["exist"] = 1
        main.FOUNDWORDS["good"] = 10
                
        expectedString = "Word does not exist in file.  Please Try Again."
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        self.assertEqual(False, main.findWordInFile("bad"))
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        output = output.rstrip()
        self.assertEqual(output, expectedString)
        self.assertNotEqual(output, "")
        
    # mocking input received from user, given a word that exists
    # in FOUNDWORDS, ensures that word is return from getReplacedWord
    @patch('main.input', return_value="exist")
    def test_getValidReplacedWord(self, input):
        main.FOUNDWORDS["exist"] = 1
        # expext it to return exists
        self.assertEqual(main.getReplacedWord(), "exist")
        self.assertNotEqual(main.getReplacedWord(), "exists")        
        
        
    # mocking input received from user, given words that does not exist
    # in FOUNDWORDS, ensures that loop is ran and user is asked multiple times 
    # to input a valid word...valid word is returned
    @patch('main.input', create=True)
    def test_getInValidReplacedWord(self, input):
        main.FOUNDWORDS["exist"] = 1
        input.side_effect = ["another bad word", "454", "invalid", "1", "exist"]
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        
        validWord = main.getReplacedWord()
        sys.stdout = sys.__stdout__

        #  expected 4 invalid prints
        # expext it to return exists once it reaches last item in array
        self.assertNotEqual(validWord, "another bad word")
        self.assertNotEqual(validWord, "454")
        self.assertNotEqual(validWord, "invalid")
        self.assertNotEqual(validWord, "1")
        self.assertEqual(validWord, "exist")        

    # mocking input received from user, given a word that does not exist
    # in FOUNDWORDS, checks to ensure capitlization/case-sensitivity 
    # matters when looking for word.
    @patch('main.input', create=True)
    def test_getInValidCaseSenstivityReplacedWord(self, input):
        main.FOUNDWORDS["exist"] = 1
        input.side_effect = ["Exist", "EXIST", "eXiSt", "exist"]
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 

        validWord = main.getReplacedWord()
        sys.stdout = sys.__stdout__
        
        #  expected 4 invalid prints
        # expext it to return exists once it reaches last item in array
        self.assertNotEqual(validWord, "Exist")
        self.assertNotEqual(validWord, "EXIST")
        self.assertNotEqual(validWord, "eXiSt")
        self.assertEqual(validWord, "exist")
        
    # mocking input received from user, checks to see if user provides ENTER, 
    # the program terminates
    @patch('main.input', return_value="")
    def test_getEnterExit(self, input):
        main.FOUNDWORDS["exist"] = 1
        with self.assertRaises(SystemExit) as error:
            main.getReplacedWord()
        self.assertEqual(str(error.exception), "No Words Replaced.  Exiting.")
        self.assertNotEqual(str(error.exception), "")
        self.assertNotEqual(len(str(error.exception)), 0)
        
    # mocking input received from user, checks to see if user provides a valid replacement
    # word.
    @patch('main.input', create=True)
    def test_getValidReplacementWord(self, input):
        input.side_effect = ["inv@lid", "!bad!", "!", "123", "nope!!", "good"]
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        validWord = main.getReplacementWord()
        sys.stdout = sys.__stdout__
        
        self.assertNotEqual(validWord, "inv@lid")
        self.assertNotEqual(validWord, "!bad!")
        self.assertNotEqual(validWord, "!")
        self.assertNotEqual(validWord, "123")
        self.assertNotEqual(validWord, "nope!!")
        self.assertEqual(validWord, "good")
        
    # Passed in a valid file, test to see if the file is properly created
    def test_checkFileCreation(self):
        wordToBeReplaced = "test"
        replacementWord = "happy"
        
        expectedPath = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase004.txt_MODIFIED')
        
        # assert file is not created yet
        assert os.path.exists(expectedPath) == False
        main.replaceWord(wordToBeReplaced, replacementWord, testCase004)
        # Assert if new file was created
        assert os.path.exists(expectedPath) == True
        
        # delete file after checking it has been created
        os.remove(expectedPath)
        
    # Given a simple file, check to ensure that all occurrances of one
    # word is replaced with the other word.
    def test_checkReplacedWords(self):
        wordToBeReplaced = "test"
        replacementWord = "happy"
        
        expectedPath = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase004.txt_MODIFIED')
        
        # assert file is not created yet
        assert os.path.exists(expectedPath) == False
        main.replaceWord(wordToBeReplaced, replacementWord, testCase004)
                
        self.assertEqual(main.FOUNDWORDS, {})
        main.readFile(expectedPath)
        
        self.assertEqual(main.FOUNDWORDS, {'happy':3, 'there':1, 
            'are':1, 'many':1, 'unique':1, 'words':1, 'in':1, 'here':1})
        self.assertNotEqual(main.FOUNDWORDS, {'test':3, 'there':1, 
            'are':1, 'many':1, 'unique':1, 'words':1, 'in':1, 'here':1})
        self.assertEqual(len(main.FOUNDWORDS), 8)
        self.assertNotEqual(len(main.FOUNDWORDS), 0)
    
        os.remove(expectedPath)
        
    # Given a file with the same word multiple times, ensures that only the
    # exact word (case-sensitive) is replaced and not all that match the same letters.
    def test_replaceSingleCaseSensitiveWord(self):
        wordToBeReplaced = "case"
        replacementWord = "success"
        
        expectedPath = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase012.txt_MODIFIED')
        
        main.replaceWord(wordToBeReplaced, replacementWord, testCase012)
                
        self.assertEqual(main.FOUNDWORDS, {})
        main.readFile(expectedPath)
        
        self.assertIn("success", main.FOUNDWORDS.keys())
        self.assertIn("CASE", main.FOUNDWORDS.keys())
        self.assertIn("casE", main.FOUNDWORDS.keys())
        self.assertIn("Case", main.FOUNDWORDS.keys())
        self.assertNotIn("case", main.FOUNDWORDS.keys())
        
        self.assertEqual(len(main.FOUNDWORDS), 4)
        self.assertNotEqual(len(main.FOUNDWORDS), 1)
        os.remove(expectedPath)


if __name__ == '__main__':
    unittest.main()