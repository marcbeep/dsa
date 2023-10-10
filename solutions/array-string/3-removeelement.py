"""
removeelements removes all occurrences of a specified val
in the input array nums
"""


def removeelements(nums, val):
    # Counter used to keep track of index where non-equal elements should be placed
    k = 0

    for i in range(len(nums)):
        # Check if current element not equal to specified value
        if nums[i] != val:
            # Update nums[k] with the current element
            # Ensures all non-equal elements moved to front of array and k now represents the count of elements not equal to val
            nums[k] = nums[i]
            k += 1

    # Replace the remaining elements with underscores
    for i in range(k, len(nums)):
        nums[i] = "_"

    print(k)
    print(nums)
    return k


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
removeelements(nums, val)
