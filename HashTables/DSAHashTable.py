import csv

from Heaps.DSAHeaps import DSAHeapEntry
from LinkedLists.LinkedLists import DSALinkedList


def nextPrime(start: int):
    if start % 2 == 0:
        prime = start + 1
    else:
        prime = start
    prime = prime - 2
    is_prime = False

    while not is_prime:
        prime += 2

        i = 3
        is_prime = True
        while i ** 2 <= prime ** 0.5 and is_prime:
            if prime % i == 0:
                is_prime = False
            else:
                i += 2
    return prime


def hashing(key: str, count: int) -> int:
    a = 63689
    b = 378551
    hash_idx = 0

    for i in range(len(key)):
        hash_idx = (hash_idx * a) + int(key[i])
        a *= b

    return hash_idx % count


class DSAHashEntry:
    def __init__(self, key: str, value, state: int = 1):
        # 0: Empty, 1: In use, 2: Removed
        self.key = key
        self.value = value
        self.state = state

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def get_state(self):
        return self.state

    def set_key(self, key: str):
        self.key = key

    def set_value(self, value):
        self.value = value

    def set_state(self, state: int):
        if state in [0, 1, 2]:
            self.state = state
        else:
            raise ValueError("Invalid state")


class DSAHashTable:
    def __init__(self, arr: DSALinkedList[DSAHashEntry], count: int | None = None):
        if count is None:
            count = len(arr)
        if count < len(arr):
            raise Exception("Count is less than array")
        self.count = nextPrime(count)
        self.hash_table = [None] * self.count
        self.size = 0

    def put(self, key: str, value):
        if self.size / self.count > 0.5:
            self.resize()

        index = hashing(key, self.count)
        initial_index = index
        entry = DSAHashEntry(key, value, 1)

        found = False
        while not found:
            current: DSAHashEntry | None = self.hash_table[index]

            if current is None or current.state in [0, 2]:
                self.hash_table[index] = entry
                self.size += 1
                found = True
            elif current.key == key:
                current.set_value(value)
                found = True
            else:
                index = (index + 1) % self.count
                if index == initial_index:
                    self.resize()

    def remove(self, key):
        self.get(key).set_state(2)
        self.size -= 1

    def has_key(self, key) -> bool:
        index = hashing(key, self.count)
        initial_index = index

        found = False
        while not found:
            current: DSAHashEntry | None = self.hash_table[index]

            if current is None:
                return False
            if current.get_key() == key and current.get_state() == 1:
                return True
            if current.get_state() in [1, 2]:
                index = (index + 1) % self.count
                if index == initial_index:
                    return False


    def get(self, key) -> DSAHashEntry:
        index = hashing(key, self.count)
        initial_index = index

        found = False
        while not found:
            current: DSAHashEntry | None = self.hash_table[index]

            if current is None:
                raise Exception("No such key exists")
            if current.get_key() == key and current.get_state() == 1:
                return current
            if current.get_state() in [1, 2]:
                index = (index + 1) % self.count
                if index == initial_index:
                    raise Exception("No such key exists")


def resize(self):
    old_table = self.hash_table
    new_count = nextPrime(self.count * 2)
    self.hash_table = [None] * new_count
    self.count = new_count
    self.size = 0

    for entry in old_table:
        if entry is not None and entry.state == 1:
            self.put(entry.key, entry.value)


if __name__ == "__main__":
    with open("RandomNames7000.csv") as f:
        reader = csv.reader(f)
        data = DSALinkedList(list(reader))

    data_hash_entries = [DSAHashEntry(i[0], i[1]) for i in data]
    table = DSAHashTable(DSALinkedList(data_hash_entries))
    for i in range(0,10):
        print(f"arr: {data_hash_entries[i]}; hash table: {table.get(data_hash_entries[i])}")
