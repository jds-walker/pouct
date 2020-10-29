from node import Node
from tiger import TigerProblem


if __name__ == "__main__":
    
    # tree = Node("root")
    tiger = TigerProblem()

    # tree.add_children(tiger.all_actions())
    # tree.select(tiger)


    for _ in range(10):

        print("\n\nRun simulation")


        print(tiger.rollout())
        tiger.restart()
