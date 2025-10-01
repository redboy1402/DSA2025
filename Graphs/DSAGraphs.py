import LinkedLists.LinkedLists as ll
from typing import TypeVar, Generic

T = TypeVar('T')

class DSAGraph(Generic[T]):
    def __init__(self, directional: bool = False):
        self.directional = directional
        self.edges = 0
        self.vertices = ll.DSALinkedList()

    class DSAGraphVertex:
        def __init__(self, label, value: T|None = None, links: ll.DSALinkedList = ll.DSALinkedList()):
            self.label = label
            self.links = links
            self.value = value

    def find_vertex(self, label: str) -> DSAGraphVertex | None:
        val = [v for v in self.vertices.to_list() if v.label == label]
        if not val: return None
        return val[0]

    def add_vertex(self, label, value = None) -> DSAGraphVertex:
        if label in [v.label for v in self.vertices.to_list()]:
            raise Exception(f'Vertex with label {label} exists')
        vertex = self.DSAGraphVertex(label, ll.DSALinkedList(), value)
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

    def has_vertex(self) -> bool:
        return not self.vertices.is_empty()

    def get_vertex_count(self) -> int:
        return len(self.vertices.to_list())

    def get_edge_count(self) -> int:
        return self.edges

    def get_vertex(self, label:str) -> DSAGraphVertex:
        return next(v.value for v in self.vertices.to_list() if v.label == label)

    def get_adjacent(self, label:str) -> list[DSAGraphVertex]:
        return next(v.links for v in self.vertices.to_list() if v.label == label)

    def is_adjacent(self, vertex1_label:str, vertex2_label:str):
        return vertex2_label in [v.label for v in self.get_adjacent(vertex1_label)]

    def display_as_list(self) -> None:
        for v in self.vertices.to_list():
            print(v.label)
            print(v.value)
            for vv in v.links.to_list():
                print(f"\t{vv.label}:{vv.value}")
