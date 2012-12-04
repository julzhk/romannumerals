import  unittest
thousands_looktable= {
    0: ('', '', ''),
    1: ('I', 'X', 'C'),
    2: ('II', 'XX', 'CC'),
    3: ('III','XXX','CCC' ),
    4: ('IV', 'XL', 'CD'),
    5: ('V', 'L', 'D'),
    6: ('VI', 'LX', 'DC'),
    7: ('VII', 'LXX', 'DCC'),
    8: ('VIII', 'LXXX', 'DCCC'),
    9: ('IX', 'XC', 'CM'),
}

def roman2int(x):
    return ''.join(reversed([
        thousands_looktable[
            int(digit)][power]
                for power, digit in enumerate(reversed(str(x)
        ))]))


class TestRomanNumerals(unittest.TestCase):

    def test_romans(self):
        assertions_table = [
            ('I',1),
            ('II',2),
            ('III',3),
            ('VI',6),
        ]
        for (roman,valu) in assertions_table:
            self.assertEqual(roman2int(valu),roman)

    def test_find_initial_digits(self):
        self.assertEqual(roman2int(449),'CDXLIX')
        self.assertEqual(roman2int(299),'CCXCIX')


if __name__ == '__main__':
    unittest.main()
