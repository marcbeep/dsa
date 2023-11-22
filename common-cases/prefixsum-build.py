def build_prefix_sum(nums):
    prefix_sum = [0] * (len(nums) + 1)

    for i in range(1, len(nums) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

    return prefix_sum


# usage
nums = [1, 4, 2, 10, 2, 3, 1, 0, 20]

prefix_sum_array = build_prefix_sum(nums)
print(f"prefix sum array: ", prefix_sum_array)
