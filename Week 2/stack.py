class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return 0
        return self.items[-1]

    def size(self):
        return len(self.items)

    def getStack(self):
        return self.items
# Stack testing

# s = Stack()
# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())


def isOperator(input):
    if input == '+' or input == '-' or input == '*' or input == '/':
        return True
    return False


def isOperand(input):
    if not input == "(" and not input == ")":
        if not isOperator(input):
            return True
    return False


def getPrecedence(input):
    if input == '+' or input == '-':
        return 1
    if input == '*' or input == '/':
        return 2
    return 0


def infix2Postfix(infix):
    input = list(infix)
    output = []
    stack = Stack()
    ccc = stack.getStack()
    for i in input:
        if i == "(":
            stack.push(i)
        if i == ")":
            while stack.peek() != "(":
                output.append(stack.pop())
            if stack.peek() == "(":
                stack.pop()
        if isOperand(i):
            output.append(i)
        if isOperator(i):
            while getPrecedence(stack.peek()) >= getPrecedence(i):
                if(stack.peek() != "("):
                    output.append(stack.pop())
            if getPrecedence(stack.peek()) < getPrecedence(i):
                stack.push(i)
    # finally move all the items in the stack into the output list
    while not stack.isEmpty():
        output.append(stack.pop())
    print("".join(output))


# infix2Postfix("(a+b)/(b+c)")
# infix2Postfix("((a+b)*((a+b)/b))")
