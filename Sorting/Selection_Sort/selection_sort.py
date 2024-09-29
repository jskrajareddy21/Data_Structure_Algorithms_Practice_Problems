def selection_sort(arr):
    l = len(arr)

    for i in range(l):
        min_index = i
        for j in range(i+1,l):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


unsorted_arr = [7,12,9,11,3]
result = selection_sort(unsorted_arr)
print("Selection sort array : ", result)