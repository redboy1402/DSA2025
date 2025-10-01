import LinkedLists as ll
import random

#underscore start & end
us = '\033[4m'
ue = '\033[0m'

if __name__ == '__main__':
    print("Welcome to the Linked Lists CLI")
    i = None
    linked_list = ll.DSALinkedList()
    while i != 'x':
        i = input(f"\tinsert at {us}S{ue}tart\n"
              f"\tinsert at {us}E{ue}nd\n"
              f"\tremove {us}F{ue}irst\n"
              f"\tremove {us}L{ue}ast\n"
              f"\t{us}D{ue}isplay list\n"
              f"\tcreate {us}R{ue}andom list\n"
              f"\te{us}X{ue}it\n"
              f"\t")
        match i.lower():
            case "s":
                linked_list.insert_first(input("input value to insert\n"))
            case "e":
                linked_list.insert_last(input("input value to insert\n"))
            case "f":
                print("removed value: " + linked_list.remove_first())
            case "l":
                print("removed value: " + linked_list.remove_last())
            case "d":
                print(linked_list.to_list())
            case "r":
                amt = input("\t\thow many random values?\n\t\t")
                while not isinstance(amt, int):
                    try:
                        amt = int(amt)
                    except ValueError:
                        amt = input("\t\tplease enter an integer\n\t\t")
                for i in range(0, amt):
                    linked_list.insert_first(str(random.randint(0,100)))
            case "x":
                pass
            case _ :
                print("Unknown Input")