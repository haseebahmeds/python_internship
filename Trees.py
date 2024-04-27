class node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
def dfs_preorder(root):
    if root==None:
        return 
    print(root.data)
    dfs_preorder(root.left)
    dfs_preorder(root.right)
def dfs_inorder(root):
    if root==None:
        return 
    dfs_inorder(root.left)
    print(root.data)
    dfs_inorder(root.right)
def dfs_postorder(root):
    if root==None:
        return 
    dfs_postorder(root.left)
    dfs_postorder(root.right)        
    print(root.data)
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
dfs_inorder(root)
dfs_postorder(root)
dfs_preorder(root)

