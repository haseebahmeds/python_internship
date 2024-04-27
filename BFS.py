'''class node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
    def bfs(root):
        q=[root]
        while q:
            a=q.pop(0)
            print(a.data)
            if a.left:
                q.append(a.left)
            if a.right:
                q.append(a.right)    
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)   '''







'''d={0:[1,4],1:[0,2,3],2:[1,3],3:[1,2],4:[0,3],5:[1]}
q=[0]
vis={0}
while q:
    a=q.pop(0)
    print(a)
    for i in d[a]:
        if i not in vis:
            q.append(i)
            vis.add(i)'''



d={0:[1,4],1:[0,2,3],2:[1,3],3:[1,2,4],4:[0,3],5:[0]}
q=[0]
vis={0}
while q:
    a=q.pop(0)
    print(a)
    for i in d[a]:
        if i not in vis:
            q.append(i)
            vis.add(i)