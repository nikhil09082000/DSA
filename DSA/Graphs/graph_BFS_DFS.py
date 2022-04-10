def insert_node(key):
    if key in dict:
        return
    dict[key]=[]
    return
def insert_edge(k1,k2):
    if k1 not in dict:
        return
    dict[k1].append(k2)

#DFS is stack model implementation
def DFS(node,dict):
    stack=[node]
    res=[]
    while(stack!=[]):
        b=stack.pop()
        if b not in res:
            res.append(b)
            for i in dict[b]:
                stack.append(i)
    return res

#BFS is queue model implementation
def BFS(node,dict):
    que=[node]
    visited=[]
    while que!=[]:
        out=que.pop(0)
        if out not in visited:
            visited.append(out)
            for i in dict[out]:
                que.append(i)
    return visited


dict={}


insert_node(0)
insert_node(1)
insert_node(2)
insert_node(3)

insert_edge(0, 1)
insert_edge(0, 2)
insert_edge(1, 2)
insert_edge(2, 0)
insert_edge(2, 3)
insert_edge(3, 3)

print(dict)

print(DFS(1,dict))
print(BFS(2,dict))