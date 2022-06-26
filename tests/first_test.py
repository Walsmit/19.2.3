import pytest
from app.calculator import Calculator


class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculator_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculator_failed(self):
        assert self.calc.multiply(self, 3, 2) == 6

    def test_division_calculator_correctly(self):
        assert self.calc.division(self, 10, 5) == 2

    def test_subraction_calculator_correctly(self):
        assert self.calc.subraction(self, 100, 40) == 60

    def test_adding_calculator_correctly(self):
        assert self.calc.adding(self, 1, 9) == 10
