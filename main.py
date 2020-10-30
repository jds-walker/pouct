from node import Node
from tiger import TigerProblem


if __name__ == "__main__":
    

    tiger = TigerProblem()
    tree = Node(tiger)

    # tree.add_children()

    print(tree.select(tree.N))

    for _ in range(1000):
        print(tree.select(tree.N))


    tree.print_tree()



