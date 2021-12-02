
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader('Tests/Data/Additiondata.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Number 2'], row['Number 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtract_method_calculator(self):
        test_data = CsvReader('Tests/Data/Subtractiondata.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Number 2'], row['Number 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply_method_calculator(self):
        test_data = CsvReader('Tests/Data/Multiplicationdata.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Number 2'], row['Number 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_divide_method_calculator(self):
        test_data = CsvReader('Tests/Data/Divisiondaata.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Number 2'], row['Number1']), result)
            self.assertEqual(self.calculator.result, result)
