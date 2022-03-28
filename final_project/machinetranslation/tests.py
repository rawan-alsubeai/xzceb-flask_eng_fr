import unittest
from  translator import french_to_english,english_to_french
class tastenglishToFrench(unittest.TestCase):
    def test1(self): 
        text= None
        masg="enter text"
        self.assertNotEqual(english_to_french(text),masg)
    def test2(self):
        eng="Hello"
        frch="Bonjour"
        self.assertEqual(english_to_french(eng),frch)


class testfrenchToEnglish(unittest.TestCase):
    def test3(self):
        text2= None
        masg2="enter text"
        self.assertNotEqual(french_to_english(text2),masg2)
    def test4(self): 
        eng2="Hello"
        frch2="Bonjour"
        self.assertEqual(french_to_english(frch2),eng2)   
   
       
if  __name__ == "__main__":
    unittest.main()
