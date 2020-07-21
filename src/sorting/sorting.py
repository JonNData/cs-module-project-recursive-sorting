# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i_a = 0
    b_i = 0
    i = 0
    while i_a < len(arrA) and b_i < len(arrB):
        if arrA[i_a] < arrB[b_i]:
            merged_arr[i] = arrA[i_a]
            i += 1
            i_a += 1
        else:
            merged_arr[i] = arrB[b_i]
            i += 1
            b_i += 1

    while i_a < len(arrA):
        merged_arr[i] = arrA[i_a]
        i += 1
        i_a += 1

    while b_i < len(arrB):
        merged_arr[i] = arrB[b_i]
        i += 1
        b_i += 1

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

