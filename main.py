from node import Node
from tiger import TigerProblem
from tiger import Action



if __name__ == "__main__":

    tiger = TigerProblem()
    tree = Node(tiger)

    # Train
    for _ in range(100000):
        tree.problem.restart()
        tree.select(tree.N)

    # Test
    rewards = []
    for _ in range(1000):
        tree.problem.restart()


        rewards.append(tree.play())
    
    print(sum(rewards)/len(rewards))



