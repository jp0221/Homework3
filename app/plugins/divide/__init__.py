from decimal import Decimal
from app.commands import Command
from calculator import Calculator


class DivideCommand(Command):
    def execute(self):
        a = Decimal(input("> First Number: "))
        b = Decimal(input("> Second Number: "))
        result = Calculator.divide(a, b)
        print(f"The result of {a} / {b} is {result}")
        