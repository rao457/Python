class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.idx = -1
    def buildTree(self, arr):
        self.idx += 1
        if(self.idx >= len(arr) or arr[self.idx] == -1 ):
            return None
        root = Node(arr[self.idx])
        root.left = self.buildTree(arr) # type: ignore
        root.right = self.buildTree(arr) # type: ignore
        return root
    def preOrder(self, root):
        if (root == None):
            return
        print(root.data , end=" ")
        self.preOrder(root.left) # type: ignore
        self.preOrder(root.right) # type : ignore
    def levelOrder(self, root):
        if (root == None):
            return None
        q = []
        q.append(root)
        q.append(None)
        while(len(q) != 0):
            temp = q.pop(0)
            if (temp == None):
                print()
                if (len(q) == 0):
                    break
                
                else:
                    q.append(None)
            else:
                print(temp.data, end= " ")
                if (temp.left != None):
                    q.append(temp.left)
                if (temp.right != None):
                    q.append(temp.right)
tree = Tree()
nodes = [1, 2, 3, 4, 5, -1, 7, -1, -1, 6, -1, -1, -1, -1, 8]
root = tree.buildTree(nodes)
tree.levelOrder(root)
# tree.preOrder(root)
