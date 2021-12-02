
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_results_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add(self):
        test_data = CsvReader('testdata/Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Number 2'], row['Number 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtract(self):
        test_data = CsvReader('Tests/Data/Subtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Number 2'], row['Number 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply(self):
        test_data = CsvReader('Tests/Data/Multiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Number 2'], row['Number 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_divide(self):
        test_data = CsvReader('Tests/Data/Division.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Number 2'], row['Number1']), result)
            self.assertEqual(self.calculator.result, result)
