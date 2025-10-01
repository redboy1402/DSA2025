from LinkedLists.LinkedLists import DSALinkedList


class DSAStack:
    def __init__(self):
        self.items = DSALinkedList()

    def push(self, item):
        self.items.insert_first(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.items.remove_first()

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.items.peek_first

    def is_empty(self):
        return self.items.is_empty()

class DSALinkedQueue:
    def __init__(self):
        self.items = DSALinkedList()
        self.count = 0

    def __iter__(self):
        while not self.is_empty:
            yield self.pop()

    def is_empty(self):
        return self.items.is_empty()

    def push(self, item):
        self.items.insert_last(item)

    def pop(self):
        self.items.remove_first()
