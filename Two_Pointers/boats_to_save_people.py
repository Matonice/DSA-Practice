"""You are given an integer array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:

Input: people = [5,1,4,2], limit = 6

Output: 2
Explanation:
First boat [5,1].
Second boat [4,2].

Example 2:

Input: people = [1,3,2,3,2], limit = 3

Output: 4
Explanation:
First boat [3].
Second boat [3].
Third boat [1,2].
Fourth boat [2].

Constraints:

1 <= people.length <= 50,000
1 <= people[i] <= limit <= 30,000"""

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        result = 0
        left, right = 0, len(people) -1

        while left <= right:
            remainder = limit - people[right]
            right -= 1
            result += 1

            if left <= right and remainder >= people[left]:
                left += 1
        
        return result