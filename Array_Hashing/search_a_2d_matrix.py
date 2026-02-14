"""You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
Example 2:

nput: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000

"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1
        while top <= bottom:
            middle_row = (top + bottom) // 2
            if target > matrix[middle_row][-1]:
                top = middle_row + 1
            elif target < matrix[middle_row][0]:
                bottom = middle_row - 1
            else:
                break

        if not (top <= bottom):
            return False

        middle_row = (top + bottom) //2
        left, right = 0, columns - 1
        while left <= right:
            middle = (left + right) // 2
            if target > matrix[middle_row][middle]:
                left = middle + 1
            elif target < matrix[middle_row][middle]:
                right = middle - 1
            else:
                return True

        return False