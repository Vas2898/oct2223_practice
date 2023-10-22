class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        print(len(self.queue))

q = Queue()
q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
q.display()
q.dequeue()
q.display()
