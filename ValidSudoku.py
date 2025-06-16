# Time Complexity: O(N^2), N is the size of the board
# Space Complexity: O(N^2)
# Did this code successfully run on Leetcode: Yes

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = 9

        rows = [set() for _ in range(size)]
        cols = [set() for _ in range(size)]
        boxes = [set() for _ in range(size)]

        for row in range(size):
            for col in range(size):
                value = board[row][col]
                if value != ".":

                    # check if the value is in rows
                    if value in rows[row]:
                        return False
                    
                    rows[row].add(value)

                    # check if the value is in columns
                    if value in cols[col]:
                        return False
                    
                    cols[col].add(value)

                    # check if the value is in boxes
                    row_idx = row // 3 
                    col_idx = col // 3
                    box = row_idx * 3 + col_idx

                    if value in boxes[box]:
                        return False
                    
                    boxes[box].add(value)
        
        return True