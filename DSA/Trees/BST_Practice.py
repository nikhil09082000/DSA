class Node:
    def __init__(self,root):
        self.data=root
        self.left=None
        self.right=None
def insert(root,key):
    if root is None:
        root=Node(key)
        return root
    else:
        if root.data==key:
            return
        if root.data<key:
            root.right=insert(root.right,key)
        if root.data>key:
            root.left=insert(root.left,key)
    return root

def lvl(root):
    q=[root]
    res=[]
    while(q!=[]):
        tm=[]
        n_q=[]
        for i in q:
            tm.append(i.data)
            if i.left is not None:
                n_q.append(i.left)
            if i.right is not None:
                n_q.append(i.right)
        res.append(tm)
        q=n_q
    return res
def right_min(root):
    cur=root
    while cur.left is not None:
        cur=cur.left
    return cur

def deletion(root,key):
    if root is None:
        return root
    elif root.data<key:
        root.right=deletion(root.right,key)
    elif root.data>key:
        root.left=deletion(root.left,key)
    else:
        if root.right is None and root.left is None:
            root=None
        elif root.right is None:
            root=root.left
        elif root.left is None:
            root=root.right
        else:
            fg=right_min(root.right)
            root.data=fg.data
            root.right= deletion(root.right,fg.data)
    return root





root=Node(10)
insert(root,5)
insert(root,15)
insert(root,3)
insert(root,8)
insert(root,11)
insert(root,18)
insert(root,7)
insert(root,14)
insert(root,2)
print(lvl(root))
deletion(root,20)
print(lvl(root))