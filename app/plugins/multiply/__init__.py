from decimal import Decimal
from app.commands import Command
from calculator import Calculator


class MultiplyCommand(Command):
    def execute(self):
        a = Decimal(input("> First Number: "))
        b = Decimal(input("> Second Number: "))
        result = Calculator.multiply(a, b)
        print(f"The result of {a} * {b} is {result}")
        