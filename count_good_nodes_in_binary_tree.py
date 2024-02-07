# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_node):
            
            if not node:
                return 0
            
            good = 1 if node.val >= max_node else 0
            max_node = max(max_node, node.val)
            good += dfs(node.left, max_node)
            good += dfs(node.right, max_node)
            
            return good
        max_node = float('-inf')
        return dfs(root, max_node)
        


def create_binary_tree(elements):
    
    root = TreeNode(elements.pop(0))
    queue = [root]
    
    while elements:
        node = queue.pop(0)
        left_val = elements.pop(0) if elements else None
        right_val = elements.pop(0) if elements else None
        if left_val is not None:
            node.left = TreeNode(left_val)
            queue.append(node.left)
        if right_val is not None:
            node.right = TreeNode(right_val)
            queue.append(node.right)
    return root

sol = Solution()

root = [3,1,4,3,None,1,5]

root = create_binary_tree(root)

print(sol.goodNodes(root))