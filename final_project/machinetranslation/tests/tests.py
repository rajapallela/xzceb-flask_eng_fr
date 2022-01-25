import unittest
import json

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'.
        self.assertNotEqual(english_to_french(' '), 'Ok')  # test when null string is given as input the output is not null string.

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.
        self.assertNotEqual(french_to_english(' '), 'Ok')  # test when null string is given as input the output is not null string.

unittest.main()
