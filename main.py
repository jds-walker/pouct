from node import Node
from tiger import TigerProblem


if __name__ == "__main__":
    
    tree = Node("root")

    tiger = TigerProblem()

    tree.add_children(tiger.all_actions())


    tiger.set_action(tree.select().data)
    print(tiger.action)
    tiger.get_observation()
    print(tiger.observation)
    
    print("\n\nRun simulation")
    while tiger.terminal == False:
        tiger.get_action()
        print(tiger.action)
        tiger.get_observation()
        print(tiger.observation)
        tiger.get_reward()
        print(tiger.reward)

    print(tiger.all_actions())