import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multyply(self):
        assert self.calc.multiply(self,2, 2) == 4
    def test_multyply(self):
        assert self.calc.multiply(self,2, 2) == 5

    def test_division(self):
        assert self.calc.division(self, 2, 2) == 1
    def test_division(self):
        assert self.calc.division(self, 2, 2) == 0

    def test_substraction(self):
        assert self.calc.division(self, 2, 2) == 0
    def test_substraction(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_adding(self):
        assert self.calc.division(self, 2, 2) == 4
    def test_adding(self):
        assert self.calc.division(self, 2, 2) == 5