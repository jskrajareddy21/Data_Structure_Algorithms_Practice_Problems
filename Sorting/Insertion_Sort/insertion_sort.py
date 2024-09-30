def insertion_sort(arr):
    l = len(arr)
    for i in range(1,l):
        insert_index = i
        current_value = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] > current_value:
                arr[j+1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = current_value

    return arr


unsorted_list = [ 7, 12, 9, 11, 3]
result = insertion_sort(unsorted_list)
print("Insertion sort array : ",result)

