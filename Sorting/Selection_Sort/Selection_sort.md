**How it works**:

    1. Go through the array to find the lowest value.
    2. Move the lowest value to the front of the unsorted part of the array.
    3. Go through the array again as many times as there are values in the array.

**Manual Run Through**:

*Step 1*: We start with an unsorted array.
`[ 7, 12, 9, 11, 3]`

*Step 2*: Go through the array, one value at a time. Which value is the lowest? 3, right?
`[ 7, 12, 9, 11, 3]`

*Step 3*: Move the lowest value 3 to the front of the array.
`[ 3, 7, 12, 9, 11]`

*Step 4*: Look through the rest of the values, starting with 7. 7 is the lowest value, and already at the front of the array, so we don't need to move it.
`[ 3, 7, 12, 9, 11]`

*Step 5*: Look through the rest of the array: 12, 9 and 11. 9 is the lowest value.
`[ 3, 7, 12, 9, 11]`

*Step 6*: Move 9 to the front.
`[ 3, 7, 9, 12, 11]`

*Step 7*: Looking at 12 and 11, 11 is the lowest.
`[ 3, 7, 9, 12, 11]`

*Step 8*: Move it to the front.
`[ 3, 7, 9, 11, 12]`

Finally, the array is sorted.

**Selection Sort Implementation**:

    1. An array with values to sort.
    2. An inner loop that goes through the array, finds the lowest value, and moves it to the front of the array. This loop must loop through one less value each time it runs.
    3. An outer loop that controls how many times the inner loop must run. For an array with *n* values, this outer loop must run *n − 1* times.

**Selection Sort Time Complexity**:

Selection Sort sorts an array of n values.

On average, about *n/2* elements are compared to find the lowest value in each loop.

And Selection Sort must run the loop to find the lowest value approximately *n* times.

We get time complexity:

---
```
O(n/2 ⋅ n) = O( n^2^ )
```
---
