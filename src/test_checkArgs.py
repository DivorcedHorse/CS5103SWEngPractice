import unittest
from main import checkArguments

class TestArguments(unittest.TestCase):
    
    # Check to see if program exits if no file
    # is given and if expected output is printed.
    def test_checkNoInputFile(self):
        with self.assertRaises(SystemExit) as error:
            checkArguments([])
        self.assertEqual(str(error.exception), "ERROR : Please Provide an Input File.")
        self.assertNotEqual(str(error.exception), "ERROR : Please Provide Only a Single Input File.")
        self.assertNotEqual(len(str(error.exception)), 0)
        
    # Check to see if program exits if multiple files
    # are provided.
    def test_checkManyInputFiles(self):
        with self.assertRaises(SystemExit) as error:
            checkArguments(["OneFile.txt", "twoFile.txt"])
        self.assertEqual(str(error.exception), "ERROR : Please Provide Only a Single Input File.")
        self.assertNotEqual(str(error.exception), "ERROR : Please Provide an Input File.")
        self.assertNotEqual(len(str(error.exception)), 0)

    # Check to see if only one file is provided
    # it returns None (No error)
    def test_checkValidSingleFile(self):
        self.assertEqual(checkArguments(["valid.txt"]), None)

if __name__ == '__main__':
    unittest.main()