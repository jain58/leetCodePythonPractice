# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
                return 0
        if root.children:
            maxlevel = 1
            for child in root.children:
                maxlevel = max(maxlevel, self.maxDepth(child))
            return maxlevel + 1
        else:
            return 1
