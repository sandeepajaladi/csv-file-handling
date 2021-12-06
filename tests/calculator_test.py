import pandas as pd
import pytest

from calculator.main import Calculator

def test_calculator_add_result():
    test_data = pd.read_csv(r'C:\Users\jaladis\PycharmProjects\csv-file-handling\done_folder\Addition.csv')
    assert isinstance(test_data, object)
    for Num1,Num2,Res in test_data.items():
        # testing assert
        assert Calculator.add(Num1,Num2) == Res


def test_calculator_subtract_result():
    """testing calculator result is 0"""
    test_data = pd.read_csv(r'C:\Users\jaladis\PycharmProjects\csv-file-handling\done_folder\Subtraction.csv')
    for Num1,Num2,Res in test_data.items():
        #result = row['Result']
        assert Calculator.sub(Num1, Num2) == Res
        #if Calculator.subtraction(row['Number2'], row['Number1']) != row['Result']
        #assertEqual(calculator.subtract(row['Number2'], row['Number1']), result)
        #assertEqual(calculator.result, result)
        #return test_data


def test_calculator_multiply_result():
    test_data = pd.read_csv(r'C:\Users\jaladis\PycharmProjects\csv-file-handling\done_folder\Multiplication.csv')
    for Num1,Num2,Res in test_data.items():
        #result = row['result']
        assert Calculator.mul(Num1,Num2) == Res
        #assertEqual(calculator.multiply(row['Number2'], row['Number1']), result)
        #assertEqual(calculator.result, result)


def test_calculator_divide_result():
    test_data = pd.read_csv(r'C:\Users\jaladis\PycharmProjects\csv-file-handling\done_folder\Division-test.csv')
    for Num1,Num2,Res in test_data.items():
       # result = row.Result
        assert Calculator.div(Num1,Num2) == Res
        # assertEqual(calculator.divide(row['Number2'], row['Number1']), result)
    # assertEqual(calculator.result, result)



