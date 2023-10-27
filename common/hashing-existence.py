def has_duplicates(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


# usage
numbers = [1, 2, 3, 4, 5, 1]
if has_duplicates(numbers):
    print("duplicates true")
else:
    print("duplicates false")
