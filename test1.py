from SC_Lab_Task1 import binarySearchRecursive, binarySearchAllIndices
import unittest

class TestBinarySearch(unittest.TestCase):
    # Test case for a single occurrence of the target in the array
    def test_single_occurrence(self):
        arr = [1, 2, 3, 4, 5, 6, 7]  # A sorted array
        # Test for a target that exists in the array (4)
        self.assertEqual(binarySearchRecursive(arr, 4, 0, len(arr) - 1), 3)
        # Test for a target that does not exist in the array (10)
        self.assertEqual(binarySearchRecursive(arr, 10, 0, len(arr) - 1), -1)

    # Test case for multiple occurrences of the target in the array
    def test_multiple_occurrences(self):
        arr = [1, 2, 2, 2, 3, 4, 5]  # A sorted array with multiple occurrences of 2
        # Test to find all indices of the target (2)
        self.assertEqual(binarySearchAllIndices(arr, 2, 0, len(arr) - 1), [1, 2, 3])
        # Test for a target that does not exist in the array (6)
        self.assertEqual(binarySearchAllIndices(arr, 6, 0, len(arr) - 1), [])

    # Test case for an empty array
    def test_empty_array(self):
        # Test on an empty array for binarySearchRecursive (should return -1 as the target cannot be found)
        self.assertEqual(binarySearchRecursive([], 1, 0, -1), -1)
        # Test on an empty array for binarySearchAllIndices (should return an empty list as the target cannot be found)
        self.assertEqual(binarySearchAllIndices([], 1, 0, -1), [])

    # Test case for an array of strings
    def test_string_array(self):
        arr = ["apple", "banana", "cherry", "date", "fig", "grape"]  # A sorted array of strings
        # Test for the presence of "cherry" in the array (should return index 2)
        self.assertEqual(binarySearchRecursive(arr, "cherry", 0, len(arr) - 1), 2)
        # Test for a string "kiwi" that does not exist in the array (should return -1)
        self.assertEqual(binarySearchRecursive(arr, "kiwi", 0, len(arr) - 1), -1)
        # Test to find all indices of "banana" (should return index 1)
        self.assertEqual(binarySearchAllIndices(arr, "banana", 0, len(arr) - 1), [1])

# Run the test suite when the script is executed
if __name__ == "__main__":
    unittest.main()
