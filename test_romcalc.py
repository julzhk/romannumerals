from romcalc import *

def test_I():
    assert roman2int('I') == 1

def test_V():
    assert roman2int('V') == 5

def test_X():
    assert roman2int('X') == 10

def test_L():
    assert roman2int('L') == 50

def test_C():
    assert roman2int('C') == 100

def test_IX():
    assert roman2int('IX') == 9

def test_XXXIX():
    assert roman2int('XXXIX') == 39

def test_CCIC():
    assert roman2int('CCIC') == 299
