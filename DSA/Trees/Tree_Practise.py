class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def pre_ord(root):
    qu=[root]
    res=[]
    while qu!=[]:
        a=qu.pop()
        res.append(a.data)
        if a.right is not None:
            qu.append(a.right)
        if a.left is not None:
            qu.append(a.left)
    return res

def pre_recur(root,ans):
    if root:
        ans.append(root.data)
        pre_recur(root.left,ans)
        pre_recur(root.right,ans)
    return ans

def inord_iter(root):
    stack=[]
    res=[]
    while root is not None or stack != []:
        while root is not None:
            stack.append(root)
            root=root.left
        root=stack.pop()
        res.append(root.data)
        root=root.right
    return res


def inord_rec(root,ans):
    if root:
        inord_rec(root.left,ans)
        ans.append(root.data)
        inord_rec(root.right,ans)
    return ans

def postord_rec(root,ans):
    if root:
        postord_rec(root.left,ans)
        postord_rec(root.right,ans)
        ans.append(root.data)
    return ans

def postord_iter(root):
    st1=[root]
    res=[]
    while st1!=[]:
        a=st1.pop()
        res.append(a.data)
        if a.left is not None:
            st1.append(a.left)
        if a.right is not None:
            st1.append(a.right)
    return res[::-1]

def lvlord_tra(root):
    q=[root]
    res=[]
    while q!=[]:
        tm=[]
        nxt_q=[]
        for i in q:
            tm.append(i.data)
            if i.left is not None:
                nxt_q.append(i.left)
            if i.right is not None:
                nxt_q.append(i.right)
        res.append(tm)
        q=nxt_q
    return res

def vertical_ord_tra(root):
    node_dict={}
    node_dict[root]=0
    dict={}
    stack=[root]
    while stack!=[]:
        cur_node=stack.pop()
        cur_lvl=node_dict[cur_node]
        if cur_lvl in dict:
            tm=dict[cur_lvl]
            tm.append(cur_node.data)
        if cur_lvl not in dict:
            tm=[]
            tm.append(cur_node.data)
            dict[cur_lvl]=tm
        if cur_node.left is not None:
            stack.append(cur_node.left)
            node_dict[cur_node.left]=cur_lvl-1
        if cur_node.right is not None:
            stack.append(cur_node.right)
            node_dict[cur_node.right]=cur_lvl+1
    return dict

def top_view(root):
    node_dict={}
    node_dict[root]=0
    dict={}
    stack=[root]
    while(stack!=[]):
        cur_node=stack.pop()
        cur_lvl=node_dict[cur_node]
        if cur_lvl not in dict:
            dict[cur_lvl]=cur_node.data
        if cur_node.left is not None:
            stack.append(cur_node.left)
            node_dict[cur_node.left]=cur_lvl-1
        if cur_node.right is not None:
            stack.append(cur_node.right)
            node_dict[cur_node.right]=cur_lvl+1
    return dict


def bottom_view(root):
    node_dict={}
    node_dict[root]=0
    stack=[root]
    dict={}
    while(stack!=[]):
        cur_node=stack.pop()
        cur_lvl=node_dict[cur_node]

        dict[cur_lvl]=cur_node.data

        if cur_node.left is not None:
            stack.append(cur_node.left)
            node_dict[cur_node.left]=cur_lvl-1
        if cur_node.right is not None:
            stack.append(cur_node.right)
            node_dict[cur_node.right]=cur_lvl+1
    return dict


def left_view(root):
    q=[root]
    res=[]
    while q!=[]:
        nxt_q=[]
        tm=[]
        for i in q:
            tm.append(i.data)
            if i.left is not None:
                nxt_q.append(i.left)
            if i.right is not None:
                nxt_q.append(i.right)
        q=nxt_q
        res.append(tm[0])
    return res

def right_view(root):
    q=[root]
    res=[]
    while q!=[]:
        nxt_q=[]
        tm=[]
        for i in q:
            tm.append(i.data)
            if i.left is not None:
                nxt_q.append(i.left)
            if i.right is not None:
                nxt_q.append(i.right)
        res.append(tm[-1])
        q=nxt_q
    return res

#need to modify some what in this
def boundary_traversal(root):
    lv=left_view(root)
    rv=right_view(root)
    bv=bottom_view(root)
    bv_val=list(bv.values())
    res=lv[1:]+rv+bv_val
    return res


def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left),height(root.right))

def zigzag(root):
    q=[root]
    res=[]
    t_m=0
    while(q!=[]):
        t_m=t_m+1
        tm=[]
        next_q=[]
        for i in q:
            tm.append(i.data)
            if i.left is not None:
                next_q.append(i.left)
            if i.right is not None:
                next_q.append(i.right)
        q=next_q
        if(t_m%2==0):
            res.append(tm[::-1])
        else:
            res.append(tm)
    return res

def right_min(root):
    if root is None:
        return
    while root.right is not None:
        root=root.right
    return root






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


print("pre order traversal(iterative)",pre_ord(root))
print("pre order traversal(recursive)",pre_recur(root,[]))
print("in order traversal(recursive)",inord_rec(root,[]))
print("in order traversal(iterative)",inord_iter(root))
print("post order traversal(recursive)",postord_rec(root,[]))
print("post order traversal(iterative): ",postord_iter(root))
print("vertical order traversal: ",vertical_ord_tra(root))
print("level order traversal: ",lvlord_tra(root))
print("top view: ",top_view(root))
print("bottom view: ",bottom_view(root))
print("left view: ",left_view(root))
print("right view: ",right_view(root))
print("boundary traversal: ",boundary_traversal(root))
print("height of tree: ",height(root))
print("zig-zag traversal: ",zigzag(root))
print("right min of root: ",right_min(root).data)

