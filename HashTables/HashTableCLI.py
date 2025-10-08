from DSAHashTable import DSAHashTable, nextPrime
from Generic.CLI import CLIGenerator, input_int, try_input
from LinkedLists.LinkedLists import DSALinkedList

def get_entry(table):
    print("keys: ", table.ordered_keys)
    try_input("Key: ", table.get)

if __name__ == "__main__":
    table = DSAHashTable()

    args = DSAHashTable()
    args["_A_dd entry"] = lambda : table.put(input("Key: "), input("Value: "))
    args["_R_emove entry"] = lambda : try_input("Key: ", table.remove)
    args["_G_et entry"] = lambda : get_entry(table)
    args["show _C_ount"] = lambda : print(table.count)
    args["show _K_eys"] = lambda : print(table.ordered_keys)
    args["show _S_ize"] = lambda : print(table.size)
    args["find next _P_rime"] = lambda : print(nextPrime(input_int("val: ")))

    CLI = CLIGenerator("Welcome to the HashTable CLI!", args).run()
