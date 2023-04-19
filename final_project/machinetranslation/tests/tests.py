import unittest
from ..translator import english_to_french,french_to_english


class TestTranslatorMethods(unittest.TestCase):

    def test_nulls(self):
       r = english_to_french(None)
       self.assertIsNone(r)
       r = french_to_english(None)
       self.assertIsNone(r)

    def test_enfr(self):
        en = "Hello"
        fr = english_to_french(en)
        self.assertEqual('Bonjour',fr)

    def test_fren(self):
        fr = "Bonjour"
        en = french_to_english(fr)
        self.assertEqual('Bonjour',fr)

    

if __name__ == '__main__':
    unittest.main()