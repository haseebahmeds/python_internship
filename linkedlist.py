'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(1)
b=node(2)
#a.next=node(2)
c=node(3)
#a.next.next=node(3)
a.next=b
b.next=c
print(a,a.data,a.next)
print(b,b.data,b.next)
print(c,c.data,c.next)'''






'''class node:
    def __init__(self,data):
        self.dta=data
        self.next=None
class sll:
    def __init__(self) ->None:
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(1)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def printing(self):
        if self.head==None:
            return
        i=self.head
        while i:
            print(i.data)
            i=i.next
l=[1,2,3,4,5]
o=sll()
for i in l:
    o.insertatbeg(i)
 '''







class node:
    def __init__(self,data):
        self.data=data
        self.next=next
class sll:
    def __init__(self) ->None:
        self.head=None
    def insertbeg(self,data):
        if self.head==None:
            self.head=node(1)  
        else:
            new=node(data)
            new.next=self.head 
            self.head=new

    def insertend(self,data):
        if self.head==None:
            self.head=new  
            return
        curr=self.head
        while(curr.next):
            curr=curr.next
        curr.next=curr  
    def removebeg(self):
        if self.head==None:
                    
