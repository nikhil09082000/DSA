class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def ispathsum(root,sum):
    ans=0
    fs=sum-root.data
    if fs==0 and root.left is None and root.right is None:
        return True
    if root.left is not None:
        ans=ispathsum(root.left,fs)
    if root.right is not None:
        ans=ispathsum(root.right,fs)
    return ans





'''
        1
    2       3
4      5  6     7
'''
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)



print(ispathsum(root,11))