from SC_Lab_Task3 import sumOfDigits  
import unittest 

class TestSumOfDigits(unittest.TestCase):
    # Test case for positive numbers
    def test_positive_numbers(self):
        # Test with a small positive number (123); expected sum of digits: 1 + 2 + 3 = 6
        self.assertEqual(sumOfDigits(123), 6)  
        # Test with a larger positive number (9876); expected sum of digits: 9 + 8 + 7 + 6 = 30
        self.assertEqual(sumOfDigits(9876), 30)  
        # Test with 0; the sum of digits should be 0
        self.assertEqual(sumOfDigits(0), 0)  

    # Test case for negative numbers
    def test_negative_numbers(self):
        # Test with a negative number (-123); the absolute value is 123, so the expected sum of digits is: 1 + 2 + 3 = 6
        self.assertEqual(sumOfDigits(-123), 6)  
        # Test with a larger negative number (-9876); the absolute value is 9876, so the expected sum of digits is: 9 + 8 + 7 + 6 = 30
        self.assertEqual(sumOfDigits(-9876), 30)  

    # Test case for large numbers
    def test_large_numbers(self):
        # Test with a large positive number (1234567890); expected sum of digits: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 0 = 45
        self.assertEqual(sumOfDigits(1234567890), 45)  
        # Test with a large negative number (-1234567890); the absolute value is 1234567890, so the expected sum of digits is 45
        self.assertEqual(sumOfDigits(-1234567890), 45)  

# Run the test suite if this script is executed directly
if __name__ == "__main__":
    unittest.main()
