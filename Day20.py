class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        for val in self.in_order(root):
            if k == 1:
                return val
            else:
                k -= 1

    def in_order(self, root):
        if root:
            for val in self.in_order(root.left):
                yield val
            yield root.val
            for val in self.in_order(root.right):
                yield val