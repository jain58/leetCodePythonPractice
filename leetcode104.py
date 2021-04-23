# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            print(root.val)
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

root = [3,9,20,None,None,15,7]
node15=TreeNode(15,None,None)
node7=TreeNode(7,None,None)
node20=TreeNode(20,15,7)
node9=TreeNode(9,None,None)
rootnode=TreeNode(3,9,20)
s = Solution()
s.maxDepth(rootnode)