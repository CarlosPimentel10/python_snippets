# Implement quicksort algorithm

def quicksort(arr):
    # define base case
    if len(arr) <= 1:
        return arr
    # Choose a pivot
    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)



arr = [3, 6, 8, 10, 1, 2, 1, 7, 8, 9]
sorted_arr = quicksort(arr)
print(f"Sorted array: {sorted_arr}")