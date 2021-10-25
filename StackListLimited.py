class Stack:
    def __init__(self,maxSize) -> None:
        self.maxSize=maxSize
        self.list=[]

    def __str__(self) -> str:
        values=reversed(self.list)
        values=[str(x) for x in values]
        return "\n".join(values)

    #isEmpty
    def isEmpty(self):
        if len(self.list)==0:
            return True
        else:
            return False

    #isFull
    def isFull(self):
        if len(self.list)==self.maxSize:
            return True
        else:
            return False

    #Push
    def push(self,value):
        if self.isFull():
            return "The stack is full"
        self.list.append(value)
        return "Element inserted successfully"

    #Pop
    def pop(self):
        if self.isEmpty():
            return "Stack already empty"
        return self.list.pop()
    
    #Peek
    def peek(self):
        if self.isEmpty():
            return "Stack already empty"
        return self.list[len(self.list)-1]

    def delete(self):
        self.list=None

cs=Stack(20)
cs.push(3)
cs.push(2)
cs.push(1)
cs.pop()
print(cs.isEmpty())
print(cs.peek())
print(cs.isFull())
print(cs)