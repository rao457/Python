class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Tree:
    def __init__(self):
        self.head = Node(None)
    def isEmpty(self):
        return self.head == None
    def append(self,val):
        self.new_Node = Node(val)
        if self.isEmpty():
            head =  self.new_Node
            return
        self.curr_node = self.head
        while(self.curr_node.next != None):
            self.curr_node = self.curr_node.next
        self.curr_node.next = self.new_Node
    def display(self):
        if self.isEmpty():
            return
        self.curr_node = self.head
        while (self.curr_node != None):
            print(self.curr_node.val + "-> ", end="")
            self.curr_node = self.curr_node.next
        print("none")
my_tree = Tree()
my_tree.append(0)
my_tree.append(2)
my_tree.append(3)
my_tree.display()
