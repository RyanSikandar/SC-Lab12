def sumOfDigits(n):
    """
    Calculates the sum of the digits of a given number using recursion.

    Args:
        n (int): The input number whose digits will be summed.

    Returns:
        int: The sum of the digits of the number.
    """
    # Ensure the number is positive to handle negative input
    n = abs(n)
    
    # Base case: when the number is reduced to 0, return 0
    if n == 0:
        return 0
    
    # Recursive case: add the last digit to the sum of the remaining digits
    return n % 10 + sumOfDigits(n // 10)
