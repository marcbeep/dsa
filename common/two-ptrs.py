def two_sum_sorted(sorted_arr, target):
    left, right = 0, len(sorted_arr) - 1

    while left < right:
        curr_sum = sorted_arr[left] + sorted_arr[right]

        if curr_sum == target:
            return [sorted_arr[left], sorted_arr[right]]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return None


# example usage
sorted_arr = [-2, 1, 2, 4, 7, 11]
target_sum = 9

result = two_sum_sorted(sorted_arr, target_sum)

if result:
    print(f"Pair with sum {target_sum}: {result}")
else:
    print("No such pair found")
