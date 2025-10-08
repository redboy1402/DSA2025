
import LinkedLists.LinkedLists as ll
from typing import TypeVar, Generic

from LinkedLists.LinkedLists import DSALinkedList, as_sorted
from LinkedLists.LinkedStacksQueues import DSALinkedQueue

T = TypeVar('T')

class DSAGraph(Generic[T]):
    def __init__(self, directional: bool = False, connections: list[tuple[str, str]] | list[str] | None = None):
        self.directional = directional
        self.edges = 0
        self.vertices: ll.DSALinkedList[DSAGraph.DSAGraphVertex] = ll.DSALinkedList()

        if connections is None:
            return

        for e in connections:
            self.add_edge(e[0], e[1])


    def __iter__(self):
        for v in self.vertices:
            yield v

    class DSAGraphVertex:
        def __init__(self, label, value: T|None = None):
            self.label = label
            self.links = DSALinkedList()
            self.value = value

        def __repr__(self):
            return f'{self.label}'

    def find_vertex(self, label: str) -> DSAGraphVertex | None:
        val = [v for v in self.vertices if v.label == label]
        if not val: return None
        return val[0]

    def add_vertex(self, label, value = None) -> DSAGraphVertex:
        if label in [v.label for v in self.vertices.to_list()]:
            raise Exception(f'Vertex with label {label} exists')
        vertex = self.DSAGraphVertex(label, value)
        self.vertices.insert_last(vertex)
        return vertex


    def add_edge(self, vertex1_label: str, vertex2_label: str) -> None:
        vertex1 = self.find_vertex(vertex1_label)
        vertex2 = self.find_vertex(vertex2_label)
        if not vertex1:
            vertex1 = self.add_vertex(vertex1_label)
        if not vertex2:
            vertex2 = self.add_vertex(vertex2_label)
        vertex1.links.insert_last(vertex2)
        self.edges += 1
        if self.directional: return
        vertex2.links.insert_last(vertex1)

    def delete_edge(self, vertex1_label: str, vertex2_label: str):
        vertex1 = self.find_vertex(vertex1_label)
        vertex2 = self.find_vertex(vertex2_label)
        if not vertex1:
            raise Exception(f"No vertex {vertex1_label} exists")
        if not vertex2:
            raise Exception(f"No vertex {vertex2_label} exists")
        if vertex2 not in vertex1.links:
            raise Exception(f"No edge exists between {vertex1_label}, {vertex2_label}")
        vertex1.links.remove_item(vertex2)
        if not self.directional:
            vertex2.links.remove_item(vertex1)

    def has_vertex(self) -> bool:
        return not self.vertices.is_empty()

    def get_vertex_count(self) -> int:
        return len(self.vertices.to_list())

    def get_edge_count(self) -> int:
        return self.edges

    def get_vertex(self, label:str) -> DSAGraphVertex:
        return next(v.value for v in self.vertices if v.label == label)

    def get_adjacent(self, label:str) -> DSALinkedList:
        return next(v.links for v in self.vertices if v.label == label)

    def is_adjacent(self, vertex1_label:str, vertex2_label:str):
        return vertex2_label in [v.label for v in self.get_adjacent(vertex1_label)]

    def display_as_list(self) -> None:
        for v in self.vertices:
            print(v.label)
            for vv in v.links:
                print(f"\t{vv.label}")

    def display_as_matrix(self) -> None:
        row = "  "
        for v in self.vertices:
            row += v.label + " "
        print(row)
        for v in self.vertices:
            row: str = v.label + " "
            for vv in self.vertices:
                if vv in v.links:
                    row += "1 "
                else:
                    row += "0 "
            print(row)

    def depth_first_search(self) -> DSALinkedQueue:
        visited = ll.DSALinkedList()
        output = DSALinkedQueue()
        first_node = as_sorted(self.vertices, key= lambda v : v.label).peek_first()
        self.DFS_visit(first_node, visited, output)
        return output

    def DFS_visit(self, vertex: DSAGraphVertex, visited, output: DSALinkedQueue):
        if vertex in visited:
            return

        visited.insert_last(vertex)
        output.push(vertex)
        for v in vertex.links:
            self.DFS_visit(v, visited, output)

    def breadth_first_search(self):
        visited = DSALinkedList()
        output = DSALinkedQueue()
        upcoming = DSALinkedQueue()
        upcoming.push(as_sorted(self.vertices, key= lambda v : v.label).peek_first())

        while not upcoming.is_empty():
            curr = upcoming.pop()
            while curr in visited:
                curr = upcoming.pop()

            for i in filter(lambda v: v not in visited, as_sorted(curr.links, key=lambda v : v.label)):
                upcoming.push(i)

            output.push(curr)
            visited.insert_first(curr)

        return output


if __name__ == "__main__":
    example1 = DSAGraph(connections=[ ("A", "B"), ("A", "D"), ("A", "C"), ("B", "E"), ("C", "D"), ("D", "F"), ("E", "F"), ("E", "G"), ("F", "G") ])
    example2 = DSAGraph(connections=[ ("A", "B"), ("A", "C"), ("A", "D"), ("B", "E"), ("C", "F"), ("D", "E"), ("D", "F"), ("D", "H"), ("E", "G"), ("F", "I"), ("H", "G"), ("H", "I"), ("H", "J")])
    print([i.label for i in example2.breadth_first_search()])
