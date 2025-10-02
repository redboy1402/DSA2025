import Generic.CLI
import DSAGraphs
from Generic.CLI import CLI_generator
from SortFilesPython.DSAsorts import merge

if __name__ == "__main__":
    graph = DSAGraphs.DSAGraph()
    args = {
        "_A_dd node": lambda : graph.add_vertex(input("Label the node\n")),
        "_D_elete node": lambda : print("unimplemented"),
        "add edge (_AE_)" : lambda : graph.add_edge(input("First node label: "), input("Second node label: ")),
        "delete edge (_DE_)" : lambda : graph.delete_edge(input("First node: "), input("Second Node: ")) (print("invalid input")),
        "display as _L_ist" : lambda : graph.display_as_list(),
        "display as _M_atrix" : lambda : graph.display_as_matrix(),
        "breadth first search (_bfs_)" : lambda : print([i.label for i in graph.depth_first_search()]),
        "depth first search (_dfs_)" : lambda : print([i.label for i in graph.breadth_first_search()])
    }
    CLI_generator(title="Welcome to the DSA Graphs CLI!", args=args).run()