def merge_sorted_arrays(arr1, arr2):
    result = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr2[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # if there are remaining elements in arr1, append them
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # if there are remaining elements in arr2, append them
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


# example usage
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

merged_arr = merge_sorted_arrays(arr1, arr2)
print("Merge sorted array: ", merged_arr)
