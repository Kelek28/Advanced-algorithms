from operator import indexOf
from turtle import pos, position


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printAll(self):
        print(self.items[::-1])


class Item:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def getValue(self):
        return self.value

    def getPriority(self):
        return self.priority


class PriorityQueue(Queue):
    def __init__(self):
        super().__init__()

    def enqueue(self, item):
        if self.isEmpty():
            return self.items.insert(0, item)
        for element in self.items:
            if element.getPriority() < item.getPriority():
                position = self.items.index(element)+1
        self.items.insert(position, item)

    def dequeue(self):
        result = self.items.pop()
        return "{} {}".format(result.getValue(), result.getPriority())

    def printAll(self):
        while not self.isEmpty():
            print(self.dequeue())


# And use the following code for testing
pq = PriorityQueue()
pq.enqueue(Item('a', 1))
pq.enqueue(Item('b', 8))
pq.enqueue(Item('c', 4))
pq.enqueue(Item('d', 10))
pq.printAll()
