from typing import TypeVar, Generic
from SortFilesPython.DSAsorts import selection_sort

T = TypeVar('T')
class DSALinkedList(Generic[T]):
    class ListItem(Generic[T]):
        def __init__(self, value: T, next_item=None, prev_item=None):
            self.prev = prev_item
            self.value = value
            self.next = next_item

        def __str__(self):
            return f"Value: {self.value}, Prev: {self.prev.get_value() if self.prev is not None else None}, Next: [{self.next if self.next is not None else None}]"

        def __repr__(self):
            return self.get_value()

        def get_prev(self):
            return self.prev

        def set_prev(self, val):
            self.prev = val

        def get_value(self):
            return self.value

        def set_value(self, value):
            self.value = value

        def get_next(self):
            return self.next

        def set_next(self, val):
            self.next = val

    def __init__(self):
        self.start = None
        self.end = None

    def __iter__(self):
        curr: DSALinkedList.ListItem | None = self.start
        while curr is not None:
            yield curr.get_value()
            curr = curr.get_next()

    def __str__(self):
        return str([*self])

    def insert_first(self, item: T):
        if self.is_empty():
            self.start = self.ListItem(item)
            self.end = self.start
        else:
            new_item = self.ListItem(item, next_item=self.start)
            self.start.set_prev(new_item)
            self.start = new_item

    def insert_last(self, item: T):
        if self.is_empty():
            self.start = self.ListItem(item)
            self.end = self.start
        else:
            new_item = self.ListItem(item, prev_item = self.end)
            self.end.set_next(new_item)
            self.end = new_item

    def is_empty(self):
        return self.start is None

    def peek_first(self) -> T:
        if self.is_empty():
            raise IndexError("List is empty")
        else:
            return self.start.get_value()

    def peek_last(self) -> T:
        if self.is_empty():
            raise IndexError("List is empty")
        else:
            return self.end.get_value()

    def remove_first(self):
        if self.is_empty():
            raise IndexError("List is empty")
        elif self.start.get_next() is None:
            tmp = self.start.get_value()
            self.end = None
            self.start = None
            return tmp
        else:
            tmp = self.start.get_value()
            self.start = self.start.get_next()
            self.start.set_prev(None)
            return tmp

    def remove_last(self):
        if self.is_empty():
            raise IndexError("List is empty")
        elif self.end.get_prev() is None:
            tmp = self.end.get_value()
            self.end = None
            self.start = None
            return tmp
        else:
            tmp = self.end.get_value()
            self.end = self.end.get_prev()
            self.end.set_next(None)
            return tmp

    def to_list(self) -> list[T]:
        out = []
        item = self.start
        while item is not None:
            out.append(item.value)
            item = item.next
        return out

    def pop_first(self) -> T:
        out = self.peek_first
        self.remove_first()
        return out

    def pop_last(self) -> T:
        out = self.peek_last
        self.remove_last()
        return out

def as_sorted(lst:DSALinkedList[T], foo=None, reverse=False) -> DSALinkedList[T]:
    new = DSALinkedList()
    #allows for lambda arguments to sort instances of a class by attribute
    if foo is not None:
        pairs = dict([(foo(i), i) for i in lst])
        old = [foo(i) for i in lst]
        for i in selection_sort(old, reverse=reverse):
            new.insert_last(pairs[i])
    else:
        old = list(lst)
        for i in selection_sort(old, reverse=reverse):
            new.insert_last(i)
    return new


if __name__ == "__main__":
    test = DSALinkedList()
    test.insert_last(1)
    test.insert_last(2)
    test.insert_last(3)
    for i in test:
        print(i.value)