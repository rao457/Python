class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    def dequeue(self):
        if (self.isEmpty()):
            raise Exception("Queue is empty")
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data
    def peek(self):
        if (self.isEmpty()):
            raise Exception("Queue is empty")
        return self.front.data
    def display(self):
        if (self.isEmpty()):
            raise Exception("Queue is empty")
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
queue.display()
print(queue.peek())    
     

    