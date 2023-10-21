"""
Given nums1 and nums 2 (int arrays sorted in 
ascending order), m (elements in nums1) and n 
(elements in nums2).

Merge nums1 and nums2 in a single array sorted
in ascending order.

Final array should be stored inside nums1.
len(nums1) = m + n

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = 
[2,5,6], n = 3 Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are 
[1,2,3] and [2,5,6]. The result of the merge 
is [1,2,2,3,5,6] with the underlined elements 
coming from nums1.

Can we come up with a O(m+n) algorithm?
"""

"""
Naive approach:
Combine the two arrays into one, then bubble sort.

def bubblesort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        # Last i elements in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped == False:
            break

def merge(nums1, nums2, m, n):
    j = 0
    print("Old: ", nums1)
    for i in range(m, m + n):
        nums1[i] = nums2[j]
        j += 1
    print("New: ", nums1)
    bubblesort(nums1)
    print("After sorting: ", nums1)

"""

"""
Efficient approach:
Compare last 2 elements, move backward
"""


def merge(nums1, nums2, m, n):
    # Last index nums1
    last = m + n - 1

    # Merge in reverse order
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1

    # Fill nums1 with leftover elements num2
    while n > 0:
        nums1[last] = nums2[n - 1]
        n, last = n - 1, last - 1

    print(nums1)


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
merge(nums1, nums2, m, n)
