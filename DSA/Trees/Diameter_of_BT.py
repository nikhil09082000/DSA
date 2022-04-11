'''
TIME COMPLEXITY: O(n^2)
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left),height(root.right))
def diameter(root):
    if root is None:
        return 0
    lheight=height(root.left)
    rheight=height(root.right)

    ldiam=diameter(root.left)
    rdiam=diameter(root.right)

    return max(lheight+rheight+1, max(ldiam,rdiam))
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
print("Tree diameter is: ",diameter(root))





