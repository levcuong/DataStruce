class Queue:
    def __init__(self):
        self.queue = list()

    def add(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No element in Queue!")

    def size(self):
        return len(self.queue)

TheQueue = Queue()
TheQueue.add("Mon")
TheQueue.add("Tue")
TheQueue.add("Wed")
print(TheQueue.size())
print(TheQueue.remove())
print(TheQueue.remove())
print(TheQueue.remove())
print(TheQueue.remove())