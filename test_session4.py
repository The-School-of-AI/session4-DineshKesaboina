import random

import pytest
import os.path
import re
import inspect 
import session4
from session4 import Qualean

from decimal import Decimal
import math as m

README_CONTENT_CHECK_FOR = [
    '__init__', 
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__', 
    '__gt__', 
    '__invertsign__', 
    '__le__', 
    '__lt__', 
    '__mul__', 
    '__sqrt__', 
    '__bool__'
]

def test_readme_exists():
    '''
    Test 1
    '''
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    '''
    Test 2
    '''
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    '''
    Test 3
    '''
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    '''
    Test 4
    '''
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

    
def test_repr():
    '''
    Test 5
    '''
    a = Qualean(1)
    b = Qualean(0)
    c = Qualean(-1)

    assert 'object at' not in a.__repr__() and 'object at' not in b.__repr__() and 'object at' not in c.__repr__()

def test_fourspace():
    '''
    Test 6
    '''
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"

def test_mandatory1():
    '''
    Test 7
    '''
    c = Qualean(-1)
    c100 = 100 * c
    c1 = 0
    for i in range(100):
        c1 = c1 + c

    assert c1 == c100, "Either Addition or Multiplication or both not implemented properly!"

def test_mandatory2():
    '''
    Test 8
    '''
    d = Qualean(random.choice([-1, 0, 1]))
    while(d.imag_value < 0):
        d = Qualean(random.choice([-1, 0, 1]))
        continue
    else:
        assert d.__sqrt__() == Decimal(d.imag_value).sqrt(), "Square root not implemented properly!"

def test_mandatory3():
    '''
    Test 9
    '''
    c1 = Decimal('0')
    for i in range(1000000):
        c = Qualean(random.choice([-1, 0, 1]))
        c1 = c + c1
    
    assert m.isclose(c1, 0, abs_tol=1000) == True, "Addition of Qualean objects not set up properly!"

def test_mandatory4():
    '''
    Test 10
    '''
    q1 = Qualean(0)
    assert (q1 and q2) == False, "Short circuiting implemented incorrectly!"

def test_mandatory5():
    '''
    Test 11
    '''
    q1 = Qualean(1)
    assert (q1 or q2) == True, "Short circuiting implemented incorrectly!"

def test_add():
    ''' Test for addition of Qualean Objects 12
    '''
    a = Qualean(1)
    b = Qualean(-1)
    c = a.__add__(b)
    assert c == a + b, "Addition implemented incorrectly"

def test_mul():
    ''' Test for multiplication of Qualean Objects 13
    '''
    a = Qualean(1)
    b = Qualean(-1)
    c = a.__mul__(b)
    assert c == a * b, "Multiplication implemented incorrectly"

def test_logical_and():
    '''Test for and 14'''
    ob1 = Qualean(-1)
    ob2 = Qualean(0)
    assert (ob1 and ob2) == False, "Logical AND implemented incorrectly!"

def test_logical_or():
    '''Test for or 15'''
    ob1 = Qualean(-1)
    ob2 = Qualean(0)
    assert (ob1 or ob2) == True, "Logical OR implemented incorrectly!"

def test_str():
    '''
    Test 16
    '''
    ob1 = Qualean(-1)
    assert 'Qualean' in ob1.__str__() and  'State' in ob1.__str__() and  'Value' in ob1.__str__()

def test_equality():
    '''
    Test 17
    '''
    ob1 = Qualean(-1)
    ob2 = Qualean(1)
    assert ( ob1 == ob2 ) == False, "equality implemented incorrectly!"

def test_float():
    '''
    Test 18
    '''
    ob1 = Qualean(-1)
    assert ob1.__float__() == float(ob1.imag_value), "float convertion implemented incorrectly!"

def test_ge():
    '''
    Test 19
    '''
    ob1 = Qualean(1)
    ob2 = Qualean(0)
    assert (ob1 >= ob2) == ob1.__ge__(ob2), "greater than equal to not implemented!"

def test_gt():
    '''
    Test 20
    '''
    ob1 = Qualean(1)
    ob2 = Qualean(0)
    (ob1 > ob2) == ob1.__gt__(ob2), "greater than not implemented!"

def test_invertsign():
    '''
    Test 21
    '''
    obj4 = Qualean(-1)
    assert (-1) * obj4.imag_value == obj4.__invertsign__(), "invert sign incorrectly implemented!"

def test_le():
    '''
    Test 22
    '''
    ob1 = Qualean(1)
    ob2 = Qualean(0)
    assert (ob1 <= ob2) == ob1.__le__(ob2), "lesser than or equal to not implemented!"

def test_lt():
    '''
    Test 23
    '''
    ob1 = Qualean(1)
    ob2 = Qualean(0)
    assert (ob1 < ob2) == ob1.__lt__(ob2), "lesser than not implemented!"

def test_bool():
    '''
    Test 24
    '''
    ob1 = Qualean(1)
    ob1 != False, "Boolean implemented incorrectly!"


def test_add_with_exceptions():
    ob1 = Qualean(1)
    with pytest.raises(ValueError):
        ob1 + 5

def test_eq_with_exceptions():
    ob1 = Qualean(1)
    with pytest.raises(TypeError):
        ob1 == 5

def test_ge_with_exceptions():
    ob1 = Qualean(1)
    with pytest.raises(TypeError):
        ob1 >= 5

def test_gt_with_exceptions():
    ob1 = Qualean(1)
    with pytest.raises(TypeError):
        ob1 > 5

def test_le_with_exceptions():
    ob1 = Qualean(1)
    with pytest.raises(TypeError):
        ob1 <= 5

def test_lt_with_exceptions():
    ob1 = Qualean(1)
    with pytest.raises(TypeError):
        ob1 < 5

def test_mul_with_exceptions():
    ob1 = Qualean(1)
    with pytest.raises(ValueError):
        ob1 * 5

def test_complex():
    d = Qualean(-1)
    while(d.imag_value > 0):
        d = Qualean(-1)
        continue
    else:
        assert isinstance(d.__sqrt__(), complex), "Complex numbers not returned for negative imaginary values! "

if __name__ == '__main__':
    test_fourspace()
