import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    result = []
    if not root:
        return result

    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        depth_size = q.qsize()
        current_level = []
        
        for _ in range(depth_size):
            node = q.get()
            current_level.append(node.val)
            
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        
        result.append(current_level)
    
    return result
def inorder(root):
    inorder(root.left)
    print(root.value)
    inorder(root.right)

def preorder(root):
    print(root.value)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    postorder(root.left)
    postorder(root.right)
    print(root.value)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(preorder(root))
