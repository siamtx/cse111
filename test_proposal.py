#  This is the test file for exam.py
from exam import twh_one, twh_two, twh_three, twh_four, twh_five, twh_six, \
twh_seven, twh_eight, twh_nine, twh_ten, twh_eleven, twh_twelve
import pytest


def test_twh_one():
    assert twh_one >= 48 <= 122


def test_twh_two():
    assert twh_two >= 48 <= 122


def test_twh_three():
    assert twh_three >= 48 <= 122
   
def test_twh_four():
    assert twh_four >= 48 <= 122
   

def test_twh_five():
    assert twh_five>= 48 <= 122
   

def test_twh_six():
    assert twh_six>= 48 <= 122


def test_twh_seven():
    assert twh_seven >= 48 <= 122


def test_twh_eight():
    assert twh_eight >= 48 <= 122

def test_twh_nine():
    assert twh_nine >= 48 <= 122


def test_twh_ten():
    assert twh_ten >= 48 <= 122


def test_twh_elven():
    assert twh_eleven >= 48 <= 122


def test_twh_twelve():
    assert twh_twelve > chr(48)
    assert twh_twelve < chr(122)




# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])