def max_sum_subarray(nums, k):
    max_sum = float("-inf")
    current_sum = 0

    # calc sum of first k elements
    for i in range(k):
        current_sum += nums[i]

    # slide the window through the array
    for i in range(k, len(nums)):
        max_sum = max(max_sum, current_sum)
        current_sum += nums[i] - nums[i - k]

    # check sum of the last window
    max_sum = max(max_sum, current_sum)

    return max_sum


# usage
nums = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 3

result = max_sum_subarray(nums, k)
print(f"max sum of a subarray of size {k}: {result}")
