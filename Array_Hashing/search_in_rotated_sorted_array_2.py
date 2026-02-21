"""You are given an array of length n which was originally sorted in non-decreasing order (not necessarily with distinct values). It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return true if target is in nums, or false if it is not present.

You must decrease the overall operation steps as much as possible.

Example 1:

Input: nums = [3,4,4,5,6,1,2,2], target = 1

Output: true
Example 2:

Input: nums = [3,5,6,0,0,1,2], target = 4

Output: false
Constraints:

1 <= nums.length <= 5000
-10,000 <= target, nums[i] <= 10,000
nums is guaranteed to be rotated at some pivot.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                left += 1

        return False