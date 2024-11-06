import unittest
from calc import calculate

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(5, 3, "+"), 8)

    def test_subtraction(self):
        self.assertEqual(calculate(10, 4, "-"), 6)

    def test_multiplication(self):
        self.assertEqual(calculate(2, 3, "*"), 6)

    def test_division(self):
        self.assertEqual(calculate(10, 2, "/"), 5)

    def test_division_by_zero(self):
        self.assertEqual(calculate(10, 0, "/"), "Ошибка: деление на ноль")

    def test_unknown_operation(self):
        self.assertEqual(calculate(5, 3, "^"), "Ошибка: неизвестная операция")

if __name__ == '__main__':
    unittest.main()
