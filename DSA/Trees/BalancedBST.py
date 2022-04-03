class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def sortedarrtoBlnceTree(arr):
    if not arr:
        return None
    n=len(arr)
    mid=n//2
    root=Node(arr[mid])
    root.left=sortedarrtoBlnceTree(arr[:mid])
    root.right=sortedarrtoBlnceTree(arr[mid+1:])
    return root

def lvl(root):
    que=[root]
    res=[]
    while(que!=[]):
        nxt_que=[]
        tmp=[]
        for i in que:
            tmp.append(i.data)
            if i.left is not None:
                nxt_que.append(i.left)
            if i.right is not None:
                nxt_que.append(i.right)
        res.append(tmp)
        que=nxt_que
    return res

arr=[11,8,9,10,1,2,3,4,5,6,7]
root=sortedarrtoBlnceTree(arr)
print(lvl(root))
