# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left if left else right
        
        
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


def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


root = [3,5,1,6,2,0,8,None,None,7,4]
root = create_binary_tree(root)
p = 5
q = 1
p = find_node(root,5)
q = find_node(root,1)
sol = Solution()
result = sol.lowestCommonAncestor(root, p, q)
print(result.val)
