class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, value):
        self.value = value

    def setNext(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head

    def add(self, node):
        temp = Node(node)
        if self.isEmpty():
            self.head = temp
            temp.setNext(self.head)
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next = temp

    # def insert(self, index, item):

    # def getSize(self):
    #     return len(self.head)
    # def search(self, item):

    def print(self):
        # print all the nodes of the list
        for nodes in self.head:
            print(nodes)


ll = LinkedList()

ll.add('a')
ll.add("b")
ll.add("c")

ll.print()
