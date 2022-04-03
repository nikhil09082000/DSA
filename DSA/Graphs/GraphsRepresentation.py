def insrt_node(key):
    if key  in graph:
        return
    else:
        graph[key]=[]
def insert_edge(a,b):
    if a not in graph or b not in graph:
        return
    else:
        graph[a].append(b)

def DFS_iter(node,grapgh,ans):
    if node not in graph:
        return
    if node not in ans:
        ans.add(node)
        for i in grapgh[node]:
            DFS_iter(i,graph,ans)


def DFS(node,graph):
    visited=set()
    stack=[node]
    while(stack!=[]):
        pp=stack.pop()
        if pp not in visited:
            visited.add(pp)
            l=graph[pp]
            for i in l:
                stack.append(i)
    return visited





graph={}
node=insrt_node('a')
insrt_node('b')
insrt_node('c')
insrt_node('d')
insrt_node('e')
insrt_node('f')
insert_edge('a','b')
insert_edge('b','d')
insert_edge('b','e')
insert_edge('e','d')
insert_edge('a','c')
insert_edge('c','d')
insert_edge('d','b')
insert_edge('d','e')
insert_edge('d','c')
insert_edge('c','f')
insert_edge('f','c')
insert_edge('d','f')
insert_edge('f','d')
print(graph)
print(DFS('a',graph))
ans= set()
DFS_iter('a',graph,ans)
print(ans)
# a---b
# |   |   e
# c---d
#   f