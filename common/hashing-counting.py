def count_elements(nums):
    element_count = {}

    # count the occurrences of each element
    for num in nums:
        element_count[num] = element_count.get(num, 0) + 1

    return element_count


# usage
numbers = [1, 2, 3, 4, 1, 2, 2, 3, 4, 5]
result = count_elements(numbers)
print("element counts: ")
for num, count in result.items():
    print(f"{num}:{count}")
