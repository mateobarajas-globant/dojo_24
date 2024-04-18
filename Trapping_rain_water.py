def trapped_water(arr):
    n = len(arr)
    if n <= 2:
        return 0
    
    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    water_trapped = 0
    
    while left < right:
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water_trapped += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water_trapped += right_max - arr[right]
            right -= 1
    
    return water_trapped

arr1 = [3, 0, 0, 2, 0, 4]
print("Example 1 Output:", trapped_water(arr1))  # Output: 10
