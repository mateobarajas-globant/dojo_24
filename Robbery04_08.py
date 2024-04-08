def rob(nums):
    if not nums:
        return 0
    
    p_max = 0
    prev_max = 0
    
    for num in nums:
        curr_max = max(p_max + num, prev_max)
        p_max = prev_max
        prev_max = curr_max
    return curr_max

nums = [2, 7, 9, 3, 1]
print(rob(nums))