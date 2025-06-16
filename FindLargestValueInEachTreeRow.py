# Time Complexity: O(N), N is the number of nodes in the binary tree
# Space Complexity: O(N/2) => O(N)
# Did this code successfully run on Leetcode: Yes


from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if root is None:
            return result

        queue = deque()
        queue.append(root)
        
        while len(queue):
            size = len(queue)
            print(size)
            largest = queue[0].val

            for _ in range(size):
                popped = queue.popleft()

                if popped.val > largest:
                    largest = popped.val
                
                if popped.left:
                    queue.append(popped.left)
                
                if popped.right:
                    queue.append(popped.right)
            
            result.append(largest)
        
        return result



