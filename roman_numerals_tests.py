import  unittest
from romcalc import RomanNumeral

degenerate_roman_lookup = {
    'IIII':'IV',
    'IVI':'V',
    'VIII': 'IX',
    'IXI': 'X'
    }

def simplify(x):
    while True:
        for complicated, simple in degenerate_roman_lookup.items():
            if x.startswith(complicated):
                rest = complicated[len(simple):]
                x = simple + rest
                break
        else:
            return x

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

    def test_simplify(self):
        self.assertEqual(simplify('IIII'), 'IV')


if __name__ == '__main__':
    unittest.main()
