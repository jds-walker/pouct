from random import choice
from enum import Enum
from tiger import TigerProblem

class Node:

    def __init__(self, problem: TigerProblem, tier=1):
        self.problem = problem
        self.N = 0 # visitation count
        self.V = 0 # score of state
        self.children = dict()
        self.tier = tier # 1 . Action 0 . Observation

    def select(self):
        if len(self.children) == 0: #do rollout and update N and V
            self.N += 1
            self.V = self.problem.rollout()
        else: 
            max_key = max(self.children, key=lambda n:  self.children[n].V)
            max_value = self.children[max_key].V
            max_keys = [k for k, v in self.children.items() if v.V == max_value]            
            child = choice(max_keys)
            self.children[child].act(child)
    

    def act(self, action):
        self.problem.set_action(action)
        observation = self.problem.get_observation()
        if observation in self.children:
            self.children[observation].select()
        else:
            self.children[observation] = Node(self.problem, tier=0) # Obtain first observation
            self.children[observation].add_children()
        
    def add_children(self):
        for action in self.problem.all_actions():
            self.children[action] = Node(self.problem)
        

    def print_tree(self):

        if len(self.children) > 0:
            for k, v in self.children.items():
                print(k)
                v.print_tree()


