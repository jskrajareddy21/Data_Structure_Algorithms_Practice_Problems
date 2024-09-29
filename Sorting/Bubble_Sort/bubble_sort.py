def bubble_sort(arr):
    l = len(arr)

    for outer in range(l):
        for i in range(l-1-outer):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]

    return arr



unsorted_arr = [7, 12, 9, 11, 3]
result = bubble_sort(unsorted_arr)
print("Bubble sorted array : ", result)