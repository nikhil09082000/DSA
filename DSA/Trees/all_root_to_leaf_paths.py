class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


#Using inorder traversal

#tm=[]
def all_root_to_leaf_paths(root,stack,tm):
    if root:
        stack.append(root.data)

        all_root_to_leaf_paths(root.left,stack,tm)

        if root.left is None and root.right is None:
            print(stack)
            tm.append(stack[:])

        all_root_to_leaf_paths(root.right,stack,tm)

        stack.pop()
    return tm

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.right.right.left=Node(10)
root.right.right.right=Node(12)
print(all_root_to_leaf_paths(root,[],[]))
#print(tm)
