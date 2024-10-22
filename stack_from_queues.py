class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head is None
    def push(self,data):
    
        new_node = Node(data)
        if (self.isEmpty()):
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if (self.isEmpty()):
            raise Exception("List is empty")
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next
        currNode = None
        
    def peek(self):
        if (self.isEmpty()):
            raise Exception("List is empty")
        currNode = self.head
        while currNode != None:
            print(currNode.data , end=" ")
            currNode = currNode.next
        print()
    def display(self):
        if (self.isEmpty()):
            return
        currNode = self.head
        while currNode:
            print(currNode.data, end=" -> ")
            currNode = currNode.next
        print()
list = LinkedList()
list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.display()