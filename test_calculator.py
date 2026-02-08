import pytest
from calculator import Calculator

def test_addition():
    calc = Calculator()
    calc.input_digit("2")
    calc.set_operator("+")
    calc.input_digit("3")
    calc.calculate()
    assert calc.get_display() == "5"

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

def test_divide_by_zero():
    calc = Calculator()
    calc.input_digit("5")
    calc.set_operator("/")
    calc.input_digit("0")
    with pytest.raises(ValueError):
        calc.calculate()