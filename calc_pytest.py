import pytest
from calc import calculate

def test_addition():
    assert calculate(5, 3, "+") == 8

def test_subtraction():
    assert calculate(10, 4, "-") == 6

def test_multiplication():
    assert calculate(2, 3, "*") == 6

def test_division():
    assert calculate(10, 2, "/") == 5

def test_division_by_zero():
    assert calculate(10, 0, "/") == "Ошибка: деление на ноль"

def test_unknown_operation():
    assert calculate(5, 3, "^") == "Ошибка: неизвестная операция"
