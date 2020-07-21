# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # input is already sorted (or empty)
    # It's recursive so we'll need to call it, figure what to call on
    # Return the index, else... -1
    # Your code here
    
    # base case
    if end >= start:
        midpoint = (end + start) // 2
        if target == arr[midpoint]:
            return midpoint
    
        elif target > arr[midpoint]:
            return binary_search(arr, target, midpoint + 1, end)
        elif target < midpoint:
            return binary_search(arr, target, start, midpoint - 1)

    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here

