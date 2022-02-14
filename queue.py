'''A python class to implement a queue data structure'''

class Queue:

    def __init__(self, *args):
        self.queue = []
        i = 0 
        while i < len(args):
            self.queue.append(args[i])
            i += 1

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return "Queue is empty"
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)



print("Creating a queue...\n")
myq = Queue(1,2,3,4)
print("Size of the queue is : " + str(myq.size()))
print("Adding element to the queue...\n")
myq.enqueue('a')
print("Displaying the queue...\n")
myq.display()
print("Removing an element....")
myq.dequeue()
print("Displaying the queue...\n")
myq.display()
print("Size of the queue is : " + str(myq.size()))
