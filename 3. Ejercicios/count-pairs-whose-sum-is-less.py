def countPairs(nums, target):
    # Write your code here
    nums.sort()
    count = 0
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            count += right - left
            left += 1
        else:
            right -= 1

    return count