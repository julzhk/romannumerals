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
    assert RomanNumeral('CCIC').i == 299

def test_CCXCIX():
    assert RomanNumeral('CCXCIX') == 299

def test_IaddI():
    a = RomanNumeral('I') + RomanNumeral('I')
    assert a == 2 and a == 'II'

def test_IiaddI():
    a = RomanNumeral('I')
    a += RomanNumeral('I')
    assert a == 2 and a == 'II'

def test_IXaddI():
    a = RomanNumeral('IX') + RomanNumeral('I')
    assert a == 10 and a == 'X'

def test_IXiaddI():
    a = RomanNumeral('IX')
    a += RomanNumeral('I')
    assert a == 10 and a == 'X'

def test_XsubI():
    a = RomanNumeral('X') - RomanNumeral('I')
    assert a == 9 and a == 'IX'

def test_XisubI():
    a = RomanNumeral('X')
    a -= RomanNumeral('I')
    assert a == 9 and a == 'IX'
