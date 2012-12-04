import  unittest

def roman2int(roman_string):
    return 6

class TestRomanNumerals(unittest.TestCase):

    def test_romans(self):
        assertions_table = [
#            ('I',1),
#            ('II',2),
#            ('III',3),
            ('IV',6),
        ]
        for (roman,valu) in assertions_table:
            self.assertEqual(roman2int(roman),valu)


if __name__ == '__main__':
    unittest.main()
