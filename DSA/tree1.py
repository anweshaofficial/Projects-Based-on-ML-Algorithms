#Question based on queue 

#BFS Tree Traversal 

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def BFS(root):
    if not root: 
        return [] 
    result, queue = [], [root]
    while queue: 
        level = [] 
        for i in range(len(queue)):
            node = queue.pop()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level.append(level)
        result.append(level)
    return result 


#Test Cases

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(BFS(root))

