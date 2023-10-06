def removeelements(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            # Partition 
            nums[k] = nums[k]
            k += 1

    print (k)
    return k


nums = [1, 3, 4, 5, 6, 7, 3, 2, 4]
val = 4
removeelements(nums,val)