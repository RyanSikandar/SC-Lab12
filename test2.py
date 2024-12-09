from SC_Lab_Task2 import ExpressionParser 
import unittest  

class TestExpressionParser(unittest.TestCase):
    # Test case for basic arithmetic operations (addition, subtraction, multiplication, division)
    def test_basic_operations(self):
        # Test addition operation
        self.assertAlmostEqual(ExpressionParser("3 + 5").evaluateExpression(), 8)
        # Test subtraction operation
        self.assertAlmostEqual(ExpressionParser("10 - 4").evaluateExpression(), 6)
        # Test multiplication operation
        self.assertAlmostEqual(ExpressionParser("6 * 7").evaluateExpression(), 42)
        # Test division operation
        self.assertAlmostEqual(ExpressionParser("8 / 4").evaluateExpression(), 2)

    # Test case to verify operator precedence (multiplication and division should be evaluated before addition and subtraction)
    def test_operator_precedence(self):
        # Test an expression where multiplication should occur before addition
        self.assertAlmostEqual(ExpressionParser("3 + 5 * 2").evaluateExpression(), 13)
        # Test an expression where division should occur before subtraction
        self.assertAlmostEqual(ExpressionParser("10 - 6 / 2").evaluateExpression(), 7)

    # Test case to verify that parentheses are correctly handled to change the order of operations
    def test_parentheses(self):
        # Test an expression where parentheses are used to prioritize addition before multiplication
        self.assertAlmostEqual(ExpressionParser("(3 + 5) * 2").evaluateExpression(), 16)
        # Test an expression with parentheses altering the order of subtraction
        self.assertAlmostEqual(ExpressionParser("10 - (2 + 3)").evaluateExpression(), 5)

    # Test case to verify that floating-point numbers are parsed and evaluated correctly
    def test_floating_point(self):
        # Test addition with floating-point numbers
        self.assertAlmostEqual(ExpressionParser("3.5 + 2.5").evaluateExpression(), 6.0)
        # Test multiplication with floating-point numbers
        self.assertAlmostEqual(ExpressionParser("5.5 * 2").evaluateExpression(), 11.0)

    # Test case for handling invalid expressions and checking error handling
    def test_invalid_expressions(self):
        # Test an expression that ends with an operator, should raise a ValueError
        with self.assertRaises(ValueError):
            ExpressionParser("3 + ").evaluateExpression()
        # Test mismatched parentheses (missing closing parenthesis), should raise a ValueError
        with self.assertRaises(ValueError):
            ExpressionParser("(3 + 5").evaluateExpression()
        # Test division by zero, should raise a ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            ExpressionParser("8 / 0").evaluateExpression()

# Run the test suite if this script is executed directly
if __name__ == "__main__":
    unittest.main()
