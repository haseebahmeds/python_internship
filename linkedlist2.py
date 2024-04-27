class node:
    def __init__(self,data):
        self.data=data
        self.next=next
        self.prev=prev
class dll:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def insertbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def printing(self):
        i=self.head
        while i:
            print(i.data)
            i.next=new 
o=dll()
for i in range(1,6):
    o.insertbeg(i)
o.printing()         
         
  
 
  