def moveZeroes(nums):
    n = len(nums)
    left = 0  
    for i in range(n):
        if nums[i] != 0:
            nums[left] = nums[i]
            left += 1
    for i in range(left, n):
        nums[i] = 0
