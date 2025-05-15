from typing import List

""" Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""

def hasDuplicate(nums: List[int]) -> bool:
    nums.sort()
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False

print(hasDuplicate([1,2,3,3]))
print(hasDuplicate([1,2,3,4]))