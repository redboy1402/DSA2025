import Generic.CLI
import DSAGraphs
from Generic.CLI import CLIGenerator
from HashTables.DSAHashTable import DSAHashTable
from LinkedLists.LinkedLists import DSALinkedList
from SortFilesPython.DSAsorts import merge

if __name__ == "__main__":
    graph = DSAGraphs.DSAGraph()
    args = DSAHashTable(DSALinkedList())
    args["_A_dd node"] = lambda : graph.add_vertex(input("Label the node\n")),
    args["_D_elete node"] = lambda : print("unimplemented"),
    args["add edge (_AE_)"] = lambda : graph.add_edge(input("First node label: "), input("Second node label: ")),
    args["delete edge (_DE_)"] = lambda : graph.delete_edge(input("First node: "), input("Second Node: ")) (print("invalid input")),
    args["display as _L_ist"] = lambda : graph.display_as_list(),
    args["display as _M_atrix"] = lambda : graph.display_as_matrix(),
    args["breadth first search (_BFS_)"] = lambda : print([i.label for i in graph.depth_first_search()]),
    args["depth first search (_DFS_)"] = lambda : print([i.label for i in graph.breadth_first_search()])

    CLIGenerator(title="Welcome to the DSA Graphs CLI!", my_args=args).run()