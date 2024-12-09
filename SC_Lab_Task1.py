def binarySearchRecursive(arr, target, left, right):
    """
    Recursively searches for the target in a sorted array.

    Args:
        arr (list): The sorted array to search within.
        target: The value to find in the array.
        left (int): The starting index of the search range.
        right (int): The ending index of the search range.

    Returns:
        int: The index of the target value if found, or -1 if the target is not present.
    """
    if arr is None or len(arr) == 0:  # Check if the array is empty or not defined
        return -1
    
    if left > right:  # Base case: the search range is invalid, meaning the target is not found
        return -1

    mid = left + (right - left) // 2  # Calculate the middle index to avoid potential overflow

    if arr[mid] == target:  # Check if the middle element matches the target
        return mid
    
    elif arr[mid] > target:  # If the middle element is greater than the target, search in the left half
        return binarySearchRecursive(arr, target, left, mid - 1)
    else:  # If the middle element is less than the target, search in the right half
        return binarySearchRecursive(arr, target, mid + 1, right)


def binarySearchAllIndices(arr, target, left, right):
    """
    Finds all indices where the target appears in a sorted array.

    Args:
        arr (list): The sorted array to search within.
        target: The value to find in the array.
        left (int): The starting index of the search range.
        right (int): The ending index of the search range.

    Returns:
        list: A list of all indices where the target is found, or an empty list if not present.
    """
    if arr is None or len(arr) == 0:  # Check if the array is empty or not defined
        return []

    if left > right:  # Base case: the search range is invalid, so the target is not found
        return []

    mid = left + (right - left) // 2  # Calculate the middle index to avoid potential overflow

    if arr[mid] == target:  # If the target is found at the middle index
        indices = [mid]  # Start a list to store the current index
        
        # Search for the target in the left sub-array and add any found indices to the list
        indices.extend(binarySearchAllIndices(arr, target, left, mid - 1))
        
        # Search for the target in the right sub-array and add any found indices to the list
        indices.extend(binarySearchAllIndices(arr, target, mid + 1, right))
        
        # Return the list of all found indices, ensuring they are sorted
        return sorted(indices)
    
    elif arr[mid] > target:  # If the target is smaller than the middle value, search the left sub-array
        return binarySearchAllIndices(arr, target, left, mid - 1)
    else:  # If the target is larger than the middle value, search the right sub-array
        return binarySearchAllIndices(arr, target, mid + 1, right)
