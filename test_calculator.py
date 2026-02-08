import pytest
from calculator import Calculator

def test_addition():
    calc = Calculator()
    calc.input_digit("2")
    calc.set_operator("+")
    calc.input_digit("3")
    calc.calculate()
    assert calc.get_display() == "5"
    
def test_subtraction():
    calc = Calculator()
    calc.input_digit("5")
    calc.set_operator("-")
    calc.input_digit("3")
    calc.calculate()
    assert calc.get_display() == "2"
    
def test_multiplication():
    calc = Calculator()
    calc.input_digit("15")
    calc.set_operator("-")
    calc.input_digit("7")
    calc.calculate()
    assert calc.get_display() == "8"
    
def test_division():
    calc = Calculator()
    calc.input_digit("9")
    calc.set_operator("/")
    calc.input_digit("3")
    calc.calculate()
    assert calc.get_display() == "3"
    
def test_negative():
    calc = Calculator()
    calc.input_digit("1")
    calc.input_digit("0")
    calc.flip_sign()
    calc.set_operator("+")
    calc.input_digit("4")
    calc.calculate()
    assert calc.get_display() == "-6"

def test_chained_operations():
    calc = Calculator()
    calc.input_digit("5")
    calc.set_operator("*")
    calc.input_digit("4")
    calc.calculate()
    calc.set_operator("+")
    calc.input_digit("2")
    calc.calculate()
    assert calc.get_display() == "22"
    
    calc.set_operator("*")
    calc.input_digit("2")
    calc.flip_sign()
    calc.calculate()
    assert calc.get_display() == "-44"

def test_divide_by_zero():
    calc = Calculator()
    calc.input_digit("5")
    calc.set_operator("/")
    calc.input_digit("0")
    with pytest.raises(ValueError):
        calc.calculate()