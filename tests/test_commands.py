"""
Testing all the commands
"""
from decimal import Decimal
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

def test_addition_functionality(monkeypatch, capfd):
    '''Testing AddCommand'''
    inputs = iter(['4', '9'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = AddCommand()
    command.execute()
    out, err = capfd.readouterr()
    expected_output = str(Decimal('4') + Decimal('9')) + '\n'
    assert out == f"The result of 4 + 9 is {expected_output}", f"Expected output was '{expected_output}', got '{out}' instead."

def test_subtraction_functionality(monkeypatch, capfd):
    '''Testing SubtractCommand'''
    inputs = iter(['5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = SubtractCommand()
    command.execute()
    out, err = capfd.readouterr()  # pylint: disable=unused-variable
    expected_output = str(Decimal('5') - Decimal('3')) + '\n'
    assert out == f"The result of 5 - 3 is {expected_output}", f"Expected output was '{expected_output}', got '{out}' instead."

def test_multiplication_functionality(monkeypatch, capfd):
    '''Testing MultiplyCommand'''
    inputs = iter(['4', '7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = MultiplyCommand()
    command.execute()
    out, err = capfd.readouterr()
    expected_output = str(Decimal('4') * Decimal('7')) + '\n'
    assert out == f"The result of 4 * 7 is {expected_output}", f"Expected output was '{expected_output}', got '{out}' instead."

def test_division_functionality(monkeypatch, capfd):
    '''Testing DivideCommand'''
    inputs = iter(['15', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = DivideCommand()
    command.execute()
    out, err = capfd.readouterr()
    expected_output = str(Decimal('15') / Decimal('5')) + '\n'
    assert out == f"The result of 15 / 5 is {expected_output}", f"Expected output was '{expected_output}', got '{out}' instead."
