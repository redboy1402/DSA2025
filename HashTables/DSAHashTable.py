import csv
from random import randint
from typing import Generic, TypeVar

T = TypeVar('T')

import numpy as np

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
        while i * i <= prime and is_prime:
            if prime % i == 0:
                is_prime = False
            else:
                i += 2
    return prime


def hashing(key: str, count: int) -> int:
    #converts any str to bytes to int to string of said int, allowing any arbitrary str to work
    conv_key = str(int.from_bytes(bytes(key, 'utf-8'), 'big'))
    a = 63689
    b = 378551
    hash_idx = 0

    for i in range(len(key)):
        hash_idx = (hash_idx * a) + int(conv_key[i])
        a *= b

    return hash_idx % count


class DSAHashEntry(Generic[T]):
    def __init__(self, key: str, value: T, state: int = 1):
        # 0: Empty, 1: In use, 2: Removed
        self.key = key
        self.value = value
        self.state = state

    def __str__(self):
        return f"{self.key}: {self.value}"

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


class DSAHashTable(Generic[T]):
    def __init__(self, arr: DSALinkedList[DSAHashEntry[T]] = DSALinkedList(), count: int | None = None):
        if count is None:
            count = len(arr)
        if count < len(arr):
            raise Exception("Count is less than array")
        self.count: int = nextPrime(count)
        self.hash_table = np.empty(shape=self.count, dtype=DSAHashEntry)
        self.ordered_keys = DSALinkedList[str]()
        self.size = 0

        for i in arr:
            self.put(i.get_key(), i.get_value())

    def __setitem__(self, key: str, value: T):
        self.put(key, value)

    def __getitem__(self, key: str):
        return self.get(key).get_value()

    def __iter__(self):
        for i in self.ordered_keys:
            yield self.get(i)

    def keys(self):
        return self.ordered_keys

    def put(self, key: str, value, add_to_keys: bool = True):
        if self.size / self.count > 0.5:
            self.resize()

        index = hashing(key, self.count)
        initial_index = index
        entry = DSAHashEntry(key, value, 1)

        found = False
        while not found:
            current: DSAHashEntry | None = self.hash_table[index]

            if current is None or current.state == 0 or current.state == 2:
                self.hash_table[index] = entry
                self.size += 1
                if add_to_keys:
                    self.ordered_keys.insert_last(key)
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
        #for i in range(len(self.ordered_keys)):
         #   if key == self.ordered_keys[i]:
          #      self.ordered_keys.remove_item(self.ordered_keys[i])

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
        return False

    def get(self, key) -> DSAHashEntry:
        index = hashing(key, self.count)
        initial_index = index

        found = False
        while not found:
            current: DSAHashEntry | None = self.hash_table[index]

            if current is None:
                raise Exception("No such key exists")
            elif current.get_key() == key and current.get_state() == 1:
                return current
            elif current.get_state() == 1 or current.get_state() == 2:
                index = (index + 1) % self.count
                if index == initial_index:
                    raise Exception("No such key exists")

    def resize(self):
        old_table = self.hash_table
        new_count = nextPrime(self.count * 2)
        self.hash_table = np.empty(shape=new_count, dtype=DSAHashEntry)
        self.count = new_count
        self.size = 0

        for entry in old_table:
            if entry is not None and entry.state == 1:
                self.put(entry.key, entry.value, False)


if __name__ == "__main__":
    with open("RandomNames7000.csv") as f:
        reader = csv.reader(f)
        data = DSALinkedList(list(reader))

    data_hash_entries = DSALinkedList()
    for i in data:
        data_hash_entries.insert_last(DSAHashEntry(i[0], i[1]))
    table = DSAHashTable(data_hash_entries)

    for _ in range(0, 10):
        i = randint(0, len(data_hash_entries))
