from node import Node
from tiger import TigerProblem



if __name__ == "__main__":
    

    tiger = TigerProblem()
    tree = Node(tiger)

    for _ in range(10000):
        tree.problem.restart()
        print(tree.select(tree.N))


    tree.print_tree()



