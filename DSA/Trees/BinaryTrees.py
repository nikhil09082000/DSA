class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# root left right
def preorder_recur(root):
    if root:
        print(root.data, end=" ")
        preorder_recur(root.left)
        preorder_recur(root.right)


# left root right
def inorder_recur(root):
    if root:
        inorder_recur(root.left)
        print(root.data, end=" ")
        inorder_recur(root.right)


# left right root
def postorder_recur(root):
    if root:
        postorder_recur(root.left)
        postorder_recur(root.right)
        print(root.data, end=" ")


def leveorder(root):
    qu = [root]
    res = []
    while (len(qu) != 0):
        l_dat = []
        lv = []
        for i in qu:
            l_dat.append(i.data)
            if i.left is not None:
                lv.append(i.left)
            if i.right is not None:
                lv.append(i.right)
        qu = lv
        res.append(l_dat)
    return res


def inorder_iter(root):
    stack = []
    res = []
    while root is not None or stack != []:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.data)
        root = root.right
    return res


def preorder_iter(root):
    stack = [root]
    res = []
    while (len(stack) != 0):
        a = stack.pop()
        res.append(a.data)
        if a.right is not None:
            stack.append(a.right)
        if a.left is not None:
            stack.append(a.left)
    return res


# https://www.geeksforgeeks.org/iterative-postorder-traversal/?ref=lbp
def postorder_iter(root):
    fs = [root]
    ss = []
    while (fs != []):
        a = fs.pop()
        ss.append(a.data)
        if a.left is not None:
            fs.append(a.left)
        if a.right is not None:
            fs.append(a.right)
    return ss[::-1]


def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))


def vertical_order(root):
    que = [root]
    node_dict = {}
    dict = {}
    node_dict[root.data] = 0
    while len(que) > 0:
        cur_node = que.pop(0)
        tm = []
        if cur_node is not None:
            cur_lvl = node_dict[cur_node.data]
            if cur_lvl in dict:
                vl = dict[cur_lvl]
                vl.append(cur_node.data)
            else:
                tm.append(cur_node.data)
                dict[cur_lvl] = tm
            if cur_node.left is not None:
                que.append(cur_node.left)
                node_dict[cur_node.left.data] = cur_lvl - 1
            if cur_node.right is not None:
                que.append(cur_node.right)
                node_dict[cur_node.right.data] = cur_lvl + 1
    return dict


def top_view(root):
    que = [root]
    node_dict = {}
    dict = {}
    node_dict[root.data] = 0
    while len(que) > 0:
        cur_node = que.pop(0)
        tm = []
        if cur_node is not None:
            cur_lvl = node_dict[cur_node.data]
            if cur_lvl not in dict:
                tm.append(cur_node.data)
                dict[cur_lvl] = tm
            if cur_node.left is not None:
                que.append(cur_node.left)
                node_dict[cur_node.left.data] = cur_lvl - 1
            if cur_node.right is not None:
                que.append(cur_node.right)
                node_dict[cur_node.right.data] = cur_lvl + 1
    return dict.values()


# bottom view
# vertical order traversal each level last values
def bottom_view(root):
    qu = [root]
    node_dict = {}
    dict = {}
    node_dict[root] = 0
    while qu != []:
        curr_nd = qu.pop(0)
        cur_lvl = node_dict[curr_nd]
        tm = []

        tm.append(curr_nd.data)
        dict[cur_lvl] = tm

        if curr_nd.left is not None:
            qu.append(curr_nd.left)
            node_dict[curr_nd.left] = cur_lvl - 1
        if curr_nd.right is not None:
            qu.append(curr_nd.right)
            node_dict[curr_nd.right] = cur_lvl + 1
    return dict


# based on level order traversal we need to reverse every even level
def zigzag(root):
    qu = [root]
    res = []
    iu = 0
    while (qu != []):
        lv = []
        nxt_qu = []
        for i in qu:
            lv.append(i.data)
            if i.left is not None:
                nxt_qu.append(i.left)
            if i.right is not None:
                nxt_qu.append(i.right)
        if (iu % 2 == 1):
            lv = lv[::-1]
        iu = iu + 1
        qu = nxt_qu
        res.append(lv)
    return res


# right view
# level order traversal right end values
def right_view(root):
    if (root is None):
        return
    qu = [root]
    res = []
    while qu != []:
        nxt_qu = []
        lvl = []
        for i in qu:
            lvl.append(i.data)
            if i.left is not None:
                nxt_qu.append(i.left)
            if i.right is not None:
                nxt_qu.append(i.right)
        qu = nxt_qu
        res.append(lvl[-1])
    return res


def diameter(root):
    st = [root]
    res = []
    drs = []
    while (st != []):
        a = st.pop()
        res.append(a.data)
        if a.left is not None or a.right is not None:
            lh = 1 + height(a.left)
            rh = 1 + height(a.right)
            drs.append(lh + rh + 1)
        if a.right is not None:
            st.append(a.right)
        if a.left is not None:
            st.append(a.left)
    return drs


def lst_inord(root):
    if root is None:
        return []
    return lst_inord(root.left) + [root.data] + lst_inord(root.right)


def bt_to_bst(root, arr):
    if root is None:
        return
    bt_to_bst(root.left, arr)
    root.data = arr[0]
    arr.pop(0)
    bt_to_bst(root.right, arr)
    return


# def height_diam(root,ans):
# 	if root is None:
#
# def diameter_eff(root):
# 	if root is None:
# 		return 0
# 	ans=[-99999999]
# 	gh=height_diam(root,ans)
# 	return ans[0]

# left view
# level order traversal left end values


'''
			1
		   / \
		  2   3
		 / \  / \
		4   5 6  7
		     \    \
		     41   42
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(41)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(42)

'''
#Binary to BST tree conversion
#for BT to BST conversion 
#	step1: inorder traversal of tree into one list
#	step2: sort the list
#	step3: again in order traverse of tree with replace of sorted array elements

arr=lst_inord(root)
print(arr)
arr.sort()
bt_to_bst(root,arr)
print(lst_inord(root))
'''
print(lst_inord(root))
preorder_recur(root)
print(preorder_iter(root))
inorder_recur(root)
print(inorder_iter(root))
postorder_recur(root)
print(postorder_iter(root))
print()
print(height(root))
print(leveorder(root))
# print(inor(root))
print(vertical_order(root))
print(top_view(root))
print('--')
print(bottom_view(root))
print('--')
print(zigzag(root))
print('r--vw--v-down')
print(right_view(root))
print('---dr--')
print(diameter(root))
