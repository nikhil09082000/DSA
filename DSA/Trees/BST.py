class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inord_iter(root):
    stack=[]
    res=[]
    while root is not None or stack!=[]:
        while root is not None:
            stack.append(root)
            root=root.left
        root=stack.pop()
        res.append(root.data)
        root=root.right
    return res

def inord_recur(root):
    if root:
        inord_recur(root.left)
        print(root.data,end=" ")
        inord_recur(root.right)
def preord_iter(root):
    stack=[root]
    res=[]
    while(stack!=[]):
        a=stack.pop()
        res.append(a.data)
        if a.right is not None:
            stack.append(a.right)
        if a.left is not None:
            stack.append(a.left)
    return(res)

def pre_recur(root):
    if root:
        print(root.data,end=" ")
        pre_recur(root.left)
        pre_recur(root.right)

def search(root,key):
    if root is None:
        return "not found"
    if root.data==key:
        return "found"
    if root.data<key:
        return search(root.right,key)
    if root.data>key:
        return search(root.left,key)
    return

def insert(root,key):
    if root is None:
        root=Node(key)
    else:
        if root.data==key:
            return root
        elif(root.data<key):
            root.right= insert(root.right,key)
        elif(root.data>key):
            root.left= insert(root.left,key)
    return root
def right_min(root):
    cur=root
    while(cur.left) is not None:
        cur=cur.left
    return cur

def delete(root,key):
    if root is None:
        return root
    elif root.data<key:
        root.right=delete(root.right,key)
    elif root.data>key:
        root.left=delete(root.left,key)
    else:
        if root.right is None and root.left is None:
            root=None
        elif root.left is None:
            root=root.right
        elif root.right is None:
            root=root.left
        else:
            temp=right_min(root.right)
            root.data=temp.data
            root.right=delete(root.right,temp.data)
    return root


root=Node(8)
root.left=Node(3)
root.right=Node(10)
root.left.left=Node(1)
root.left.right=Node(6)
root.left.right.left=Node(4)
root.left.right.right=Node(7)
root.right.right=Node(14)
root.right.right.left=Node(13)

print(*(inord_iter(root)))
inord_recur(root)
print()
pre_recur(root)
print()
print(*(preord_iter(root)))
print()
print(search(root,13))
insert(root,2)
print()
inord_recur(root)
delete(root,2)
print()
inord_recur(root)
