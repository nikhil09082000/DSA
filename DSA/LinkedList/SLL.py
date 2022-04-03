class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def PrintData(self):
        val=[]
        tmp=self.head
        while(tmp):
            val.append(tmp.data)
            tmp=tmp.next
        return val

    def dele(self,val):
        global prev
        tmp=self.head
        if(tmp.data==val):
            self.head=tmp.next
            return

        while(tmp is not None):
            if(tmp.data==val):
                break
            prev=tmp
            tmp=tmp.next

        prev.next=tmp.next
        tmp=None

    def del_at_index(self,key):
        global prev
        tmp=self.head
        if(key==0):
            self.head=tmp.next
            return
        for i in range(key):
            prev=tmp
            tmp=tmp.next
        prev.next=tmp.next

    def add_ele_at_ind(self,ind,key):
        global prev
        nwnode=Node(key)
        tmp=self.head
        if(ind==0):
            self.head=nwnode
            nwnode.next=tmp
            return
        i=0
        while(tmp):
            prev=tmp
            tmp=tmp.next
            i += 1
            if(i==ind):
                break
        prev.next=nwnode
        nwnode.next=tmp




    def add_ele_strt(self,key):
        new=Node(key)
        new.next=self.head
        self.head=new

    def append(self,key):
        nnode=Node(key)
        tmp=self.head
        while(tmp.next):
            tmp=tmp.next
        tmp.next=nnode

    def lenn(self,node):
        if(node==None):
            return 0
        else:
            return 1+self.lenn(node.next)
    def getcount(self):
        return self.lenn(self.head)




llist=LinkedList()
llist.add_ele_strt(1)
llist.add_ele_strt(2)
llist.add_ele_strt(3)
llist.add_ele_strt(4)

llist.append(456)
#llist.dele(2)
#llist.del_at_index(0)
llist.add_ele_at_ind(4,123)
print(llist.getcount())
print(llist.PrintData())
























