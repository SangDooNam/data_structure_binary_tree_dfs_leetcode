# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root):
        def dfs(node, is_left, result):
            if not node:
                return result - 1
            
            if is_left:
                return max(dfs(node.left, False, result + 1), dfs(node.right, True, 1))
            else:
                return max(dfs(node.right, True, result + 1), dfs(node.left, False, 1))
            
        return max(dfs(root.left, False, 1), dfs(root.right, True, 1))



def create_binary_tree(elements):
    root = TreeNode(elements.pop(0))
    queue = [root]
    
    while queue:
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



root = [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1]
root = create_binary_tree(root)

sol = Solution()
print(sol.longestZigZag(root))