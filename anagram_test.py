"""
Test for Anagram Class
"""
try:
    from anagram import Anagram
except ImportError:
    raise SystemExit('anagram.py is not exist!')

import unittest

class AnagramTests(unittest.TestCase):
    def test_no_matches(self):
        self.assertEqual(
            False,
            Anagram().is_anagram_of('bowery', 'bowfin')
        )

    def test_detect_simple_anagram(self):
        self.assertEqual(
            True,
            Anagram().is_anagram_of('adders', 'dreads')
        )

if __name__ == '__main__':
    unittest.main()