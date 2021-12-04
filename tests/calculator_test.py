import pandas as pd
from calculator.main import Calculator


def test_calculator_add_result():
    """testing calculator result is 0"""
    test_data = pd.read_csv(r'C:\Users\jaladis\PycharmProjects\csv-file-handling\testdata\Addition.csv')
    for row in test_data:
        result = row['Result']
        assert Calculator.add(row.Number2, row.Number1) == row.Result
        #assertEqual(calculator.add(row['Number2'], row['Number1']), result)
        #assertEqual(calculator.result, result)


def test_calculator_subtract_result():
    """testing calculator result is 0"""
    test_data = pd.read_csv('testdata/Subtraction.csv')
    for row in test_data:
        result:float = float(row['Result'])
        assert Calculator.subtract(row["Number2"], row["Number1"]) == row["result"]
        #assertEqual(calculator.subtract(row['Number2'], row['Number1']), result)
        #assertEqual(calculator.result, result)


def test_calculator_multiply_result():
    """testing calculator result is 0"""
    test_data = pd.read_csv('testdata/Multiplication.csv')
    for row in test_data:
        result: float = float(row['result'])
        assert Calculator.multiply(row["Number2"], row["Number1"]) == row["result"]
        #assertEqual(calculator.multiply(row['Number2'], row['Number1']), result)
        #assertEqual(calculator.result, result)


def test_calculator_divide_result():
    """testing calculator result is 0"""
    test_data = pd.read_csv('testdata/Division-test.csv', sep = ",")
    i=0
    for row in test_data:
       # result = row.Result
        assert Calculator.division(row) == row.Result
        i = i+1
    # assertEqual(calculator.divide(row['Number2'], row['Number1']), result)
    # assertEqual(calculator.result, result)


'''def test_calculator_divide_fail_result(self):
    """testing calculator result is 0"""
    test_data = pd.read_csv('Tests/Data/Division.csv').data
    for row in test_data:
        result = float(row['Result'])
        self.assertEqual(self.calculator.divide(row['Number 2'], 0), result)
        assert result == "Error: A number cannot be divided by 0" '''
