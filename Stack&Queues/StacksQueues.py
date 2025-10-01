from abc import abstractmethod, ABC

from numpy.ma.extras import dstack


class DSAStack:
    def __init__(self, size=100):
        self.items = [""] * size
        self.size = size
        self.count = 0

    def push(self, item):
        if self.isFull():
            raise IndexError("Stack is full")
        else:
            self.items[self.count] = item
            self.count += 1
            #print(f"added  {item}\t count {self.count}\t items {self.items}")


    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            out = self.items[self.count - 1]
            self.count -= 1
            #print(f"popped {out}\t count {self.count}\t items {self.items}")
            return out

    def top(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            return self.items[self.count - 1]

    def getCount(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

class _DSAQueue(ABC):
    def __init__(self, size=100):
        self.items = [""] * size
        self.size = size
        self.count = 0

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def isFull(self):
        pass

    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def getCount(self):
        pass

class DSACircularQueue(_DSAQueue):
    def __init__(self, size=100):
        super().__init__(size)
        self.front = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size - 1

    def push(self, item):
        if self.isFull():
            raise IndexError("Queue is full")
        self.items[(self.front + self.count) % self.size] = item
        self.count += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        tmp = self.items[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return tmp

    def getCount(self):
        return self.count

class DSAShufflingQueue(_DSAQueue):
    def __init__(self, size=100):
        super().__init__(size=size)

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

    def push(self, item):
        if self.isFull():
            raise IndexError("Queue is full")
        self.items[self.count] = item
        self.count += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        tmp = self.items[0]
        for i in range(1, self.count):
            self.items[i-1] = self.items[i]
        self.count -= 1
        return tmp

    def getCount(self):
        return self.count

def parse_infix_to_postfix(infix: str) -> _DSAQueue:
    infix = infix.split(" ")
    postFix = DSACircularQueue()
    opStack = DSAStack()

    for token in infix:
        if token == "(":
            opStack.push("(")

        elif token == ")":
            while opStack.top() != "(":
                postFix.push(opStack.pop())
            opStack.pop()

        elif token in "+-*/":
            while (not opStack.isEmpty()) and opStack.top() != "(" and _precedence(opStack.top()) >= _precedence(token):
                postFix.push(opStack.pop())
            opStack.push(token)
        else:
            postFix.push(token)

    while not opStack.isEmpty():
        postFix.push(opStack.pop())
    return postFix

def _precedence(char: chr) -> int:
    if char in "()":
        return 3
    elif char in "*/":
        return 2
    elif char in "+-":
        return 1
    else:
        return 0

def _postfix_evaluator(postfix: _DSAQueue):
    out = DSAStack()
    while not postfix.isEmpty():
        val = postfix.pop()
        match val:
            case "+":
                a = float(out.pop())
                b = float(out.pop())
                out.push(b + a)
            case "-":
                a = float(out.pop())
                b = float(out.pop())
                out.push(b - a)
            case "/":
                a = float(out.pop())
                b = float(out.pop())
                out.push(b / a)
            case "*":
                a = float(out.pop())
                b = float(out.pop())
                out.push(b * a)
            case _:
                out.push(float(val))
    return out.pop()

def eval_infix(infix: str):
    post = parse_infix_to_postfix(infix)
    return _postfix_evaluator(post)


if __name__ == "__main__":
    ex = "5 * ( 5 - 1 * ( 1 - 3 ) )"
    print(eval_infix(ex))