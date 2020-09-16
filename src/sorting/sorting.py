# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    a = 0 # Starting pointer for arrA
    b = 0 # Starting pointer for arrB

    for i in range(elements):
        # check if a is in bounds of arrA
        # The reason we do this is because we might get to a point where the pointer goes out of bounds
        if a >= len(arrA):
            # we've moved all the elements from arrA into merged_arr already
            # we still have elements from arrB that need to be moved
            merged_arr[i] = arrB[b]
            b += 1
        # check if b is in bounds of arrB
        # The reason we do this is because we might get to a point where the pointer goes out of bounds
        elif b >= len(arrB):
            # we've moved all the elements from arrB into merged_arr already
            # we still have elements from arrA that need to be moved
            merged_arr[i] = arrA[a]
            a += 1
        # Then we compare arrA[a] against arrB[b]
        elif arrA[a] < arrB[b]:
        # move the smaller element into merged_arr
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    # base case: 
    # merge sort continually splits the input array
    # until we only have single-element arrays
    # when len(arr) == 1
    # then => 
    # once the array has been split down to single element arrays
    # merge these arrays back together in sorted order using `merge`
    if len(arr) > 1:
        left = merge_sort(arr[0:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])

        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

