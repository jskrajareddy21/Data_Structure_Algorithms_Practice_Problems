**How it works**:

    1. Go through the array, one value at a time.
    2. For each value, compare the value with the next value.
    3. If the value is higher than the next one, swap the values so that the highest value comes last.
    4. Go through the array as many times as there are values in the array.

 **Manual Run**:

 *Step 1*: We start with an unsorted array
 `[7, 12, 9, 11, 3]`

 *Step 2*: We look at the two first values. Does the lowest value come first? Yes, so we don't need to swap them.
 `[7, 12, 9, 11, 3]` #compare 7 and 12

 *Step 3*: Take one step forward and look at values 12 and 9. Does the lowest value come first? No.
 `[7, 12, 9, 11, 3]`

 *Step 4*: So we need to swap them so that 9 comes first.
 `[7, 9, 12, 11, 3]`

*Step 5*: Taking one step forward, looking at 12 and 11.
`[7, 9, 12, 11, 3]`

*Step 6*: We must swap so that 11 comes before 12.
`[7, 9, 11, 12, 3]`

*Step 7*: Looking at 12 and 3, do we need to swap them? Yes.
`[7, 9, 11, 12, 3]`

*Step 8*: Swapping 12 and 3 so that 3 comes first.
`[7, 9, 11, 3, 12]`

Now right most value is the highest value in given array.
Repeat Step 2 to till end

**Bubble Sort Implementation**:

To implement the Bubble Sort algorithm in a programming language, we need:

    1. An array with values to sort.
    2. An inner loop that goes through the array and swaps values if the first value is higher than the next value. This loop must loop through one less value each time it runs.
    3. An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.

**Bubble Sort Time Complexity**:
    The Bubble Sort algorithm loops through every value in the array, comparing it to the value next to it. So for an array of
n values, there must be n such comparisons in one loop. And after one loop, the array is looped through again and again n times.

This means there are n⋅n comparisons done in total, so the time complexity for Bubble Sort is:
--
 O(n^2) 
--