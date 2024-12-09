class ExpressionParser:
    def __init__(self, expression):
        """
        Initializes the parser with the given mathematical expression.

        Args:
            expression (str): The mathematical expression as a string.
        """
        # Remove all whitespace from the expression and store the cleaned string in self.tokens
        self.tokens = expression.replace(" ", "")  
        self.index = 0  # Initialize the index to track the current position in the expression

    def evaluateExpression(self):
        """
        Evaluates the entire mathematical expression.

        Returns:
            float: The result of the expression evaluation.
        """
        # Start parsing from the addition/subtraction level
        return self.parseAdditionSubtraction()

    def parseMultiplicationDivision(self):
        """
        Parses and evaluates multiplication and division operations.

        Returns:
            float: The result of the multiplication/division operations.
        """
        # Begin parsing by handling expressions within parentheses or a number
        result = self.parseParentheses()

        # Continue parsing any multiplication or division operations
        while self.index < len(self.tokens):
            # Check if the current token is a multiplication operator
            if self.tokens[self.index] == '*':
                self.index += 1  # Move past the '*' operator
                result *= self.parseParentheses()  # Multiply the result by the next value
            # Check if the current token is a division operator
            elif self.tokens[self.index] == '/':
                self.index += 1  # Move past the '/' operator
                divisor = self.parseParentheses()  # Parse the divisor
                if divisor == 0:  # Raise an error if division by zero is attempted
                    raise ZeroDivisionError("Division by zero is not allowed.")
                result /= divisor  # Divide the result by the divisor
            else:
                break  # Exit the loop if no more multiplication/division operators are found

        return result

    def parseParentheses(self):
        """
        Parses and evaluates expressions enclosed in parentheses.

        Returns:
            float: The result of the sub-expression within the parentheses.
        """
        # Check if the current character is an opening parenthesis
        if self.tokens[self.index] == '(':
            self.index += 1  # Move past the opening parenthesis
            result = self.parseAdditionSubtraction()  # Recursively parse the expression inside parentheses
            # Ensure there is a matching closing parenthesis
            if self.index >= len(self.tokens) or self.tokens[self.index] != ')':
                raise ValueError("Mismatched parentheses.")
            self.index += 1  # Move past the closing parenthesis
            return result
        # If no parentheses, parse the number directly
        return self.parseNumber()

    def parseAdditionSubtraction(self):
        """
        Parses and evaluates addition and subtraction operations.

        Returns:
            float: The result of the addition/subtraction operations.
        """
        # Start by parsing multiplication/division, as it has higher precedence
        result = self.parseMultiplicationDivision()

        # Continue parsing any addition or subtraction operations
        while self.index < len(self.tokens):
            # Check if the current token is an addition operator
            if self.tokens[self.index] == '+':
                self.index += 1  # Move past the '+' operator
                if self.index >= len(self.tokens):  # Ensure the expression isn't incomplete
                    raise ValueError("Expression ends with an operator.")
                result += self.parseMultiplicationDivision()  # Add the next value to the result
            # Check if the current token is a subtraction operator
            elif self.tokens[self.index] == '-':
                self.index += 1  # Move past the '-' operator
                if self.index >= len(self.tokens):  # Ensure the expression isn't incomplete
                    raise ValueError("Expression ends with an operator.")
                result -= self.parseMultiplicationDivision()  # Subtract the next value from the result
            else:
                break  # Exit the loop if no more addition/subtraction operators are found

        return result

    def parseNumber(self):
        """
        Parses a number from the expression (integer or floating-point).

        Returns:
            float: The parsed number.
        """
        number_start = self.index  # Store the starting index of the number
        # Continue to move the index while the current character is part of the number (digit or '.')
        while self.index < len(self.tokens) and (self.tokens[self.index].isdigit() or self.tokens[self.index] == '.'):
            self.index += 1

        # Raise an error if no number was found at the current position
        if number_start == self.index:
            raise ValueError(f"Expected a number at index {self.index}, but found '{self.tokens[self.index]}'.")
        
        # Extract the number from the tokens and return it as a float
        return float(self.tokens[number_start:self.index])
