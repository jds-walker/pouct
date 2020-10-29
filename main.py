from node import Node
from tiger import TigerProblem


if __name__ == "__main__":
    

    tiger = TigerProblem()
    tree = Node(tiger)
    tree.add_children()

    tree.select()

    # tree.print_tree()



