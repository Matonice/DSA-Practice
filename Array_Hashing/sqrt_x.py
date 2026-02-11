"""You are given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
Example 1:

Input: x = 9

Output: 3
Example 2:

Input: x = 13

Output: 3
Constraints:

0 <= x <= ((2^31)-1)"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        result = 0

        while left <= right:
            middle = left + ((right - left)//2)
            
            if middle**2 > x:
                right = middle - 1
            elif middle**2 < x:
                left = middle + 1
                result = middle
            else:
                return middle
        
        return result
        