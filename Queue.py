class Queue:
    def __init__(self):
        self.queue=[]

    def is_empty(self):
        return len(self.queue)==0

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
           return self.queue.pop(0)

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(29)
q.enqueue(40)
q.enqueue(20)


data = q.dequeue()
print(data)
print(q.is_empty())
print(q.size())
