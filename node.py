from random import choice
from enum import Enum
from tiger import TigerProblem

class Node:



    def __init__(self, data, tier=1):
        self.data = data
        self.N = 0 # visitation count
        self.V = 0 # score of state
        self.children = dict()
        self.tier = tier # 1 . Action 0 . Observation

    def select(self, problem: TigerProblem):
        max_key = max(self.children, key=lambda n:  self.children[n].V)
        max_value = self.children[max_key].V
        max_keys = [k for k, v in self.children.items() if v.V == max_value]            
        selected = self.children[choice(max_keys)]
        if len(selected.children) == 0:
            #rolllout
            a = 1+1
            print(a)
        else: 
            print("act")
            selected.act(problem)    

    def act(self, problem: TigerProblem):
        problem.set_action(self.data)
        observation = problem.get_observation()
        if observation in self.children:
            self.children[observation].select()
        else:
            self.children[observation] = Node(observation, tier=0) # Obtain first observation
            self.children[observation].add_children(problem.all_actions())
        
    def add_children(self, children):
        for child in children:
            self.children[child] = Node(child)
        

    def print_tree(self):
        print(self.data)
        if len(self.children) > 0:
            for v in self.children.values():
                v.print_tree()


