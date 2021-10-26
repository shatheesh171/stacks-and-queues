class Node:
    def __init__(self,value=None) -> None:
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

class Stack:
    def __init__(self) -> None:
        self.ll=LinkedList()

    def __str__(self) -> str:
        values=[str(x.value) for x in self.ll]
        return "\n".join(values)

    #isEmpty
    def isEmpty(self):
        if self.ll.head==None:
            return True
        return False

    #Push
    def push(self,value):
        node=Node(value)
        node.next=self.ll.head
        self.ll.head=node
       
    #Pop
    def pop(self):
        if self.ll.head is None:
            return "Empty stack" 
        node=self.ll.head
        self.ll.head=node.next
        return node.value

    #Peek
    def peek(self):
        if self.ll.head is None:
            return "Empty stack" 
        return self.ll.head.value

    #delete    
    def delete(self):
        self.ll.head=None


stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
print(stack.peek())
print(stack)