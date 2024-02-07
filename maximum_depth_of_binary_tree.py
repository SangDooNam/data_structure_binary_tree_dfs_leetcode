# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
        return max(left, right) + 1
    



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

tree =  create_binary_tree([3,9,20,None, None,15,7])

sol =Solution()
print(sol.maxDepth(tree))