# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        def dfs(node, current_sum, dct):
            if not node:
                return 0
            current_sum += node.val
            
            result = dct.get(current_sum - targetSum, 0)
            
            dct[current_sum] = dct.get(current_sum, 0) + 1
            
            result += dfs(node.left, current_sum, dct)
            result += dfs(node.right, current_sum, dct)
            
            dct[current_sum] -= 1
            
            return result
        
        dct = {0: 1}
        current_sum = 0
        return dfs(root, current_sum, dct)
            


def create_tree_list(elements):
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
    

root = [10,5,-3,3,2,None,11,3,-2,None,1]

root = create_tree_list(root)

sol = Solution()
print(sol.pathSum(root, 8))