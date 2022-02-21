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


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def getValue(self):
        return self.value

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setValue(self, value):
        self.value = value

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right


class BST:
    def __init__(self, *args):
        self.root = None
        if len(args) == 1 and isinstance(args[0], list):
            for val in args[0]:
                self.insert(val)

    def getRoot(self):
        return self.root

    def setRoot(self, root):
        self.root = root

    def insert(self, value):
        #create a new node
        node = Node(value)
        # status of insertion position
        #found = False

        if self.root == None:
            self.root = node
        else:
            par = self.root
            cur = par
            while True:
                if node.getValue() > cur.getValue():
                    cur = cur.getRight()
                    if cur == None:  # found the insertion position
                        par.setRight(node)
                        break
                else:
                    cur = cur.getLeft()
                    if cur == None:  # found the insertion position
                        par.setLeft(node)
                        break
                # not leaf, carry on
                par = cur

    def inOrderTraversal(self, cur):
        res = []
        if cur:
            res = self.inOrderTraversal(cur.getLeft())
            res.append(cur.getValue())
            res = res+self.inOrderTraversal(cur.getRight())
        return res

    def preOrderTraversal(self, cur):
        res = []
        if cur:
            res.append(cur.getValue())
            res = res + self.preOrderTraversal(cur.getLeft())
            res = res + self.preOrderTraversal(cur.getRight())
        return res

    def postOrderTraversal(self, cur):
        res = []
        if cur:
            res = self.postOrderTraversal(cur.getLeft())
            res = res + self.postOrderTraversal(cur.getRight())
            res.append(cur.getValue())
        return res

    def search(self, cur, value):

        if cur == None or cur.getValue() == value:
            return cur
        elif value > cur.getValue():
            return self.search(cur.getRight(), value)
        else:
            return self.search(cur.getLeft(), value)

    def inOrderPre(self, cur):
        if cur == None:
            return None, None
        if cur.getLeft() == None:
            return None, cur
        else:
            parpre = cur
            pre = cur.getLeft()
            while pre.getRight() != None:
                parpre = pre
                pre = pre.getRight()
            return pre, parpre

    def next(self, cur):
        if cur == None:
            return None
        elif cur.getLeft() != None:
            return cur.getLeft()
        elif cur.getRight() != None:
            return cur.getRight()
        else:
            return None

    def delete(self, value):

        if self.root == None:
            print("The tree is empty or the current root is None.")
        else:
            #search the value
            # if not found, and stop deletion
            # else return current and parent node.
            par = self.root
            cur = self.root
            pos = 0  # 0 for left and 1 for right

            while cur != None:

                if value > cur.getValue():
                    par = cur
                    pos = 1
                    cur = cur.getRight()
                elif value < cur.getValue():
                    par = cur
                    pos = 0
                    cur = cur.getLeft()
                else:
                    break

            # after the search

            if cur == None:
                print("The value isn't included in the tree.")
            else:
                #found the node
                #case1 &case2: no child or one child
                if not (cur.getLeft() != None and cur.getRight() != None):
                    if cur == self.root:
                        self.root = self.next(cur)
                    elif par.getLeft() == cur:
                        par.setLeft(self.next(cur))
                    else:
                        par.setRight(self.next(cur))
                else:
                    #case 3: two children
                    pre, parpre = self.inOrderPre(cur)
                    #delete pre
                    if parpre.getLeft() == pre:
                        parpre.setLeft(None)
                    else:
                        parpre.setRight(None)

                    cur.setValue(pre.getValue())

    def printALLNodes(self):
        # we use breadth-first to print all nodes in the tree
        queue = Queue()

        if self.root != None:
            queue.enqueue(self.root)

        while not queue.isEmpty():
            cur = queue.dequeue()
            if cur != None:
                print(cur.getValue())
                queue.enqueue(cur.getLeft())
                queue.enqueue(cur.getRight())


#tree = BST([8,3,6,1,10,14,4,7,13])
tree = BST()
tree.insert(8)
tree.insert(3)
tree.insert(6)
tree.insert(1)
tree.insert(10)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)


print("Pre-order:", tree.preOrderTraversal(tree.root))
print("In-order: ",  tree.inOrderTraversal(tree.root))
print("Post-order:", tree.postOrderTraversal(tree.root))

tree.printALLNodes()

#print(tree.search(tree.root, 13))
tree.delete(10)

tree.printALLNodes()
