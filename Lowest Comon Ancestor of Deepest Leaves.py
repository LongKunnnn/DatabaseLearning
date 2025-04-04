class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:        
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return 0, None

            left_height, left_lca = dfs(node.left)
            right_height, right_lca = dfs(node.right)

            if left_height > right_height:
                return left_height + 1, left_lca
            elif left_height < right_height:
                return right_height + 1, right_lca
            else:
                return left_height + 1, node
        _, lca = dfs(root)
        return lca