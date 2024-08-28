"""
Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
Output: Subarray with zero-sum exists
The subarrays with a sum of 0 are:
{ 3, 4, -7 }
{ 4, -7, 3 }
{ -7, 3, 1, 3 }
{ 3, 1, -4 }
{ 3, 1, 3, 1, -4, -2, -2 }
{ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
"""


# Function to check if a sublist with zero-sum is present in a given list or not
def hasZeroSumSublist(nums):
    # create an empty set to store the sum of elements of each
    # sublist `nums[0…i]`, where `0 <= i < len(nums)`
    s = set()

    # insert 0 into the set to handle the case when sublist with
    # zero-sum starts from index 0
    s.add(0)
    print(f's1 : {s}')
    total = 0

    # traverse the given list
    for i in nums:

        # sum of elements so far
        total += i

        # if the sum is seen before, we have found a sublist with zero-sum
        if total in s:
            return True

        # insert sum so far into the set
        s.add(total)
        print(f's2: {s}')

    # we reach here when no sublist with zero-sum exists
    return False


if __name__ == '__main__':

    nums = [4, -6, 3, -1, 4, 2, 7]

    if hasZeroSumSublist(nums):
        print('Sublist exists')
    else:
        print('Sublist does not exist')