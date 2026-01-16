arr = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(arr):
    ln = len(arr)

    for x in range(ln): # running the outer loop for entirety of length of the list
        for y in range(ln - 1 - x): # running the inner loop one less time compared to the last since 
                               # we have a sorted(highest) element at the end.
            if arr[y] > arr[y+1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]

    return arr

sorted_list = bubble_sort(arr)
print(f"Here's the sorted list in ascending order: {sorted_list}")