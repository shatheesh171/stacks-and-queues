from _typeshed import SupportsLessThan


class Queue:
    def __init__(self,maxSize) -> None:
        #O(n) space complexity
        self.items=maxSize*[None]
        self.maxSize=maxSize
        self.start=-1
        self.top=-1

    def __str__(self) -> str:
        values=[str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top+1==self.start:
            return True
        elif self.start==0 and self.top==self.maxSize-1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top==-1:
            return True
        return False


    def enqueue(self,value):
        if self.isFull():
            return "Queue is already full"
        if self.top+1==self.maxSize:
            self.top=0
        else:
            self.top+=1
            if self.start==-1:
                self.start=0
            self.items[self.top]=value
            return "Element inserted at end of queue"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        elem=self.items[self.start]
        start=self.start
        #Only one element
        if self.start==self.top:
            self.start=-1
            self.top=-1
        #start at last element
        elif self.start+1==self.maxSize:
            self.start=0
        else:
            self.start+=1
        self.items[start]=None
        return elem    
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.items[self.start]


    def delete(self):
        self.items=self.maxSize*[None]
        self.top=-1
        self.start=-1

cq=Queue(3)
cq.enqueue(1)
cq.enqueue(1)
cq.enqueue(1)
print(cq.isFull())
cq.dequeue()
print(cq)