class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        if self.stack1:
            self.stack1.append(x)
        else:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            self.stack1.append(x)

    def dequeue(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
q.enqueue(4)
q.dequeue(5)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())


