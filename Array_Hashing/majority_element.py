from typing import List


"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [5,5,1,1,1,5,5]

Output: 5
Example 2:

Input: nums = [2,2,2]

Output: 2"""


def majority_element(nums: List[int]) -> int:
    hash_map = {}

    for num in nums:
        hash_map[num] = hash_map.get(num,0) + 1
        if hash_map[num] > len(nums) / 2:
            return num
        

print(majority_element([5,5,1,1,1,5,5]))
print(majority_element([2,2,2]))