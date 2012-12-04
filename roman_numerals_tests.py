import  unittest
from romcalc import RomanNumeral

class TestRomanNumerals(unittest.TestCase):

    def test_romans(self):
        assertions_table = [
            ('I',1),
            ('II',2),
            ('III',3),
            ('VI',6),
        ]
        for (roman,valu) in assertions_table:
            self.assertEqual(RomanNumeral(valu),roman)

    def test_find_initial_digits(self):
        self.assertEqual(RomanNumeral(449),'CDXLIX')
        self.assertEqual(RomanNumeral(299),'CCXCIX')


if __name__ == '__main__':
    unittest.main()
