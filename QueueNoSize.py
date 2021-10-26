class Queue:
    def __init__(self) -> None:
        self.items=[]

    def __str__(self) -> str:
        values=[str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if len(self.items)==0:
            return True
        return False

    def enqueue(self,value):
        self.items.append(value)
        return "The element is inserted at end of Queue"

    def dequeue(self):
        if self.isEmpty():
            return "Queue empty"

        return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue empty"

        return self.items[0]

    def delete(self):
        self.items=None


#Custom queue
cq=Queue()
print(cq.isEmpty())
cq.enqueue(2)
cq.enqueue(1)
cq.enqueue(3)
cq.dequeue()
print(cq)
print(cq.peek())