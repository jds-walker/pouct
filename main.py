from node import Node
from tiger import TigerProblem


if __name__ == "__main__":
    

    tiger = TigerProblem()
    tree = Node(tiger)

    # tree.add_children()

    tree.select(tree.N)
    tree.select(tree.N)

    for _ in range(1000):
        tree.select(tree.N)


    tree.print_tree()



