# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [root]
        different = False
        cousinsA = False
        cousinsB = False
        while queue:
            if not cousinsA or not cousinsB:
                cousinsA = False
                cousinsB = False
            level = []
            for n in queue:
                if n.val == x: cousinsA = True
                if n.val == y: cousinsB = True
                if n.left and n.right:
                    if(x == n.left.val and y == n.right.val) or (y == n.left.val and x == n.right.val):
                        different = True
                for kid in (n.left, n.right):
                    if kid: level.append(kid)
            queue = level[:]
        return cousinsA and cousinsB and not different