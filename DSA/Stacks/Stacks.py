class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.size = 0

    def push(self,data):
        nwnode=Node(data)
        nwnode.next=self.head
        self.head=nwnode
        self.size += 1

    def get_size(self):
        return(self.size)

    def peek(self):
        return self.head.data

    def pop(self):
        tmp=self.head
        self.head=tmp.next
        self.size -= 1

    def print_list(self):
        tmp=self.head
        li=[]
        while(tmp):
            li.append(tmp.data)
            tmp=tmp.next
        return li


llist=LinkedList()

llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)

llist.pop()

print(llist.print_list())
print(llist.size)
print(llist.peek())