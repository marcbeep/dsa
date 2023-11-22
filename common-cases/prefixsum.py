# technique involves precomputing the cumulative sum


def subarray_with_target_sums(nums, target):
    prefix_sum = [0] * (len(nums) + 1)

    # calc prefix sum
    for i in range(1, len(nums) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

    # find the subarray with the target sum
    for start in range(len(nums)):
        for end in range(start + 1, len(nums) + 1):
            current_sum = prefix_sum[end] - prefix_sum[start]
            if current_sum == target:
                return nums[start:end]

    return None


# usage
nums = [1, 4, 2, 10, 2, 3, 1, 0, 20]
target_sum = 12

result = subarray_with_target_sums(nums, target_sum)
print(f"subarray with taget sum {target_sum}: {result}")
