**How it works**:

    1. Take the first value from the unsorted part of the array.
    2. Move the value into the correct place in the sorted part of the array.
    3. Go through the unsorted part of the array again as many times as there are values.

**Manual Run**:

*Step 1*: We start with an unsorted array.
`[ 7, 12, 9, 11, 3]`

*Step 2*: We can consider the first value as the initial sorted part of the array. If it is just one value, it must be sorted, right?
`[ 7, 12, 9, 11, 3]`

*Step 3*: The next value 12 should now be moved into the correct position in the sorted part of the array. But 12 is higher than 7, so it is already in the correct position.
`[ 7, 12, 9, 11, 3]`

*Step 4*: Consider the next value 9.
`[ 7, 12, 9, 11, 3]`

*Step 5*: The value 9 must now be moved into the correct position inside the sorted part of the array, so we move 9 in between 7 and 12.
`[ 7, 9, 12, 11, 3]`

*Step 6*: The next value is 11
`[ 7, 9, 12, 11, 3]`


*Step 7*: We move it in between 9 and 12 in the sorted part of the array.
`[ 7, 9, 11, 12, 3]`

*Step 8*: The last value to insert into the correct position is 3.
`[ 7, 9, 11, 12, 3]`

*Step 9*: We insert 3 in front of all other values because it is the lowest value.
`[ 3,7, 9, 11, 12]`

Finally, the array is sorted.

**Insertion Sort Implementation**:

    1. An array with values to sort.
    2. An outer loop that picks a value to be sorted. For an array with n values, this outer loop skips the first value, and must run n − 1 times.
    3. An inner loop that goes through the sorted part of the array, to find where to insert the value. If the value to be sorted is at index i, the sorted part of the array starts at index 0 and ends at index i − 1.

**Insertion Sort Time Complexity**:

Selection Sort sorts an array of n values.

On average, each value must be compared to about n/2 other values to find out where to insert it.

And Selection Sort must run the loop to insert a value in its correct place approximately n times.

We get time complexity for Insertion Sort:

---
O(n/2 ⋅ n) = O(n^2)
---
