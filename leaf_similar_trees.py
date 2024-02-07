# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        
        def dfs(node):
            
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return dfs(node.left) + dfs(node.right)
        
        return dfs(root1) == dfs(root2) 

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

# root1 = [3,5,1,6,2,9,8,None,None,7,4]
# root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
root1 = [1,2,3]
root2 = [1,3,2] 

root1 = create_binary_tree(root1)
root2 = create_binary_tree(root2)

sol = Solution()

print(sol.leafSimilar(root1))