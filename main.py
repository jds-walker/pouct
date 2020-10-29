from node import Node
from tiger import TigerProblem


if __name__ == "__main__":
    

    tiger = TigerProblem()
    tree = Node(tiger)

    tree.add_children(tiger.all_actions())
    tree.select()

    tree.print_tree()



