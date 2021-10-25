
class Stack:
    def __init__(self):
        self.list=[]

    def __str__(self):
        if len(self.list):
            print(self.list)
            return
        values=reversed(self.list)
        values=[str(x) for x in values]
        return "\n".join(values)

    #isEmpty
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    #Push
    def push(self,value):
        self.list.append(value)
        return "Element inserted in stack successfully"

    #Pop
    def pop(self):
        #print(self.list)
        if self.isEmpty():
            return "No elements in the stack"
        return self.list.pop()

    #Peek
    def peek(self):
        if self.isEmpty():
            return "No elements in the stack"
        return self.list[len(self.list)-1]

    #delete complete stack
    def delete(self):
        self.list=None

#Custom Stack
cs=Stack()
print(cs.isEmpty())
cs.push(1)
cs.push(2)
cs.push(3)
#print(cs)
cs.pop()
cs.delete()
print(cs)
print(cs.peek())