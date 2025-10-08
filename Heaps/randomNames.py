import DSAHeaps
import csv

from LinkedLists.LinkedLists import DSALinkedList

if __name__ == "__main__":
    with open("RandomNames7000(1).csv") as f:
        reader = csv.reader(f)
        data = DSALinkedList(list(reader))
    with open("RandomNames7000Output.txt", "w") as f:
        data = DSAHeaps.heapsort(data)
        out = ""
        for i in data:
            out += f"{i.priority}, {i.value}\n"
        f.write(out)