from node import Node
from tiger import TigerProblem
from tiger import Action



if __name__ == "__main__":

    tiger = TigerProblem()

    tree = Node(tiger)
    



    for _ in range(10000):
        tree.problem.restart()
        tree.select(tree.N)


    t = tree



