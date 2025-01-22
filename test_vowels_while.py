import unittest
from vowels while import count_vowels  # Make sure the import path is correct

class TestCountVowels(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfgh"), 0)

    def test_all_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_mixed_case(self):
        self.assertEqual(count_vowels("aEiOu"), 5)

    def test_mixed_characters(self):
        self.assertEqual(count_vowels("hello world"), 3)
        self.assertEqual(count_vowels("Python Programming"), 4)

    def test_numbers_and_special_chars(self):
        self.assertEqual(count_vowels("123456!@#"), 0)
        self.assertEqual(count_vowels("vow3ls!aEioU"), 5)

if __name__ == '__main__':
    unittest.main()
