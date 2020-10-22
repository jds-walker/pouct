from node import Node
from tiger import TigerProblem


if __name__ == "__main__":
    
    # n = Node("root")
    # # n.add_children()
    # for _ in range(2):
    #     n._select()

    # n.print_tree()

    # for _ in range(5):
    #     n.add_children()
    # n.print_tree()

    tiger = TigerProblem()
    print(tiger.state)
    while tiger.terminal == False:
        tiger.get_action()
        print(tiger.action)
        tiger.get_observation()
        print(tiger.observation)
        tiger.get_reward()
        print(tiger.reward)