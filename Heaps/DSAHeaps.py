from math import floor
from LinkedLists.LinkedLists import DSALinkedList


def heapsort(arr: DSALinkedList, has_value = False):
    #converts values to DSAHeapEntries
    if has_value:
        heap = DSAHeap(DSALinkedList([DSAHeapEntry(i[0], i[1]) for i in arr]))
    else:
        heap = DSAHeap(DSALinkedList([DSAHeapEntry(i) for i in arr]))
    for i in range(len(arr)-1, 0, -1):
        heap.heap_arr[0], heap.heap_arr[i] = heap.heap_arr[i], heap.heap_arr[0]
        heap.trickle_down(0, i)

    arr = [i for i in heap.heap_arr]
    return arr




class DSAHeapEntry:
    def __init__(self, priority: int, value: any = None):
        self.priority = priority
        self.value = value

    def get_priority(self):
        return self.priority

    def set_priority(self, priority: int):
        self.priority = priority

    def get_value(self):
        return self.value

    def set_value(self, value: any):
        self.value = value

class DSAHeap:
    def __init__(self, heap_arr: DSALinkedList = None):
        if heap_arr is None:
            heap_arr = DSALinkedList()
        self.heap_arr = heap_arr
        self.heapify()

    def add(self, entry: DSAHeapEntry):
        self.heap_arr.insert_last(entry)
        self.trickle_up(len(self.heap_arr) - 1)

    def remove(self):
        out = self.heap_arr[0]
        self.heap_arr[0] = self.heap_arr.pop_last()
        return out.value

    def trickle_up(self, index: int):
        cur_i: int = index
        parent_i: int = floor((cur_i-1)/2)
        while cur_i > 0 and self.heap_arr[cur_i].priority > self.heap_arr[parent_i].priority:
            self.heap_arr[parent_i], self.heap_arr[cur_i] = self.heap_arr[cur_i], self.heap_arr[parent_i]
            cur_i = parent_i
            parent_i = floor((cur_i - 1) / 2)

    def trickle_down(self, index: int, heap_size: int | None = None):
        if heap_size is None:
            heap_size = len(self.heap_arr)

        cur = index
        running = True

        while running:
            left = cur * 2 + 1
            right = left + 1
            running = False
            largest = cur

            if left < heap_size and self.heap_arr[left].priority > self.heap_arr[largest].priority:
                largest = left
            if right < heap_size and self.heap_arr[right].priority > self.heap_arr[largest].priority:
                largest = right

            if largest != cur:
                self.heap_arr[largest], self.heap_arr[cur] = self.heap_arr[cur], self.heap_arr[largest]
                cur = largest
                running = True

    def heapify(self):
        for i in range(0, floor(len(self.heap_arr) / 2))[::-1]:
            self.trickle_down(i)

    def display(self):
        print([i.value for i in self.heap_arr])

if __name__ == "__main__":
    test = DSALinkedList()
    for i in [1, 6, 3, 5, 7]:
        test.insert_last(i)
    print(test)
    print(heapsort(test))
