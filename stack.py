'''A python class to implement a stack data structure'''

class myStack:
    
    def __init__(self, *argv):
        self.stack= []
        self.top = 0 

    def createStack(self, *argv):
        self.stack = list(argv)
        self.top = len(self.stack)
        return f"stack has been piled with items : {argv} "
    
    def isEmpty(self):
        if self.top == 0:
            return "The stack is empty"
        else:
            return "The stack is not empty"

    def pop(self):
        self.stack.pop()
        self.top = len(self.stack) - 1 
        return "Item has been popped."

    def push(self, item):
        self.stack.append(item)
        self.top = len(self.stack) + 1 
        return f"Item {item} has been pushed."

    def peek(self ):
        return self.stack[-1:]

    def printStack(self):
        return (self.stack)

stack1 = myStack()

print("Creating Stack ...\n" + stack1.createStack(1,2,3,4,5))
print("Pushing a new element \"6\" to the stack.."+(stack1.push(6)))
print("Printing the stack" + str(stack1.printStack()))
print("Poping the recently pushed element \"6\" from the stack.."+str(stack1.pop()))
print("Printing the stack" + str(stack1.printStack()))
print("Checking if the stack is empty ....\t"+ str(stack1.isEmpty()))
print("Peeking the stack\t" + str(stack1.peek()))









