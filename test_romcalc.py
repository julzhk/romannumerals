from romcalc import RomanNumeral

def test_I():
    assert RomanNumeral('I') == 1

def test_V():
    assert RomanNumeral('V') == 5

def test_X():
    assert RomanNumeral('X') == 10

def test_L():
    assert RomanNumeral('L') == 50

def test_C():
    assert RomanNumeral('C') == 100

def test_IX():
    assert RomanNumeral('IX') == 9

def test_XXXIX():
    assert RomanNumeral('XXXIX') == 39

def test_CCIC():
    assert RomanNumeral('CCIC') == 299

def test_CCXCIX():
    assert RomanNumeral('CCXCIX') == 299
