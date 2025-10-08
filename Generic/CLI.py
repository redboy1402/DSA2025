from typing import Callable
from HashTables.DSAHashTable import DSAHashTable
from LinkedLists.LinkedLists import DSALinkedList

#underscore start & end
us = '\033[4m'
ue = '\033[0m'


class CLIGenerator:
    def __init__(self, title: str, my_args: DSAHashTable[Callable], init_foo = None):
        self.title = title
        self.args: DSAHashTable[Callable] = my_args
        self.args["e_X_it"] = lambda : print()
        self.validInputs = []
        if init_foo is not None:
            init_foo()

    def run(self):
        print(self.title)
        i:str = ""
        input_str = ""
        for i in self.args.keys():
            tmp = i.split("_")
            if len(tmp) != 3:
                raise Exception(f"{i} is invalid format")
            tmp = "\t" + tmp[0] + us + tmp[1] + ue + tmp[2] + "\n"
            input_str += tmp

        while i != 'x':
            found = False
            i = input(input_str).lower()
            if i == "x":
                found = True
            for k in self.args.keys():
                if i == k.split("_")[1].lower():
                    self.args[k]()
                    found = True
            if not found:
                print("Error! Invalid Input!")
        print("Program Exited")


if __name__ == '__main__':

    linked_list = DSALinkedList()

    args: DSAHashTable[Callable] = DSAHashTable(DSALinkedList())
    args.put("insert at _S_tart", lambda : linked_list.insert_first(input("input value to insert\n")))
    args.put("insert at _E_nd", lambda : linked_list.insert_last(input("input value to insert\n")))
    args.put("_D_isplay", lambda : print(linked_list.to_list()))
    CLIGenerator(title="ll CLI", my_args=args).run()