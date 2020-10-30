from random import choice
from math import sqrt
from enum import Enum
from tiger import TigerProblem

class Node:

    def __init__(self, problem: TigerProblem, exploration = 0.2, tier=1):
        self.problem = problem
        self.N = 0 # visitation count
        self.V = 0 # score of state
        self.children = dict()
        self.tier = tier # 1 . Action 0 . Observation
        self.exploration = exploration
        

    def select(self, TotalN):
        reward = None
        if len(self.children) == 0:
            #rollout
            self.add_children()
            random_action = choice(list(self.children.keys()))
            reward = self.children[random_action].observe(random_action)
        else:
            # Finds best next action then observe
            max_key = max(self.children, key=lambda n:  self.children[n].V + ((self.exploration * sqrt(TotalN/self.children[n].N)) if self.children[n].N > 0 else 0 ))
            max_value = self.children[max_key].V
            max_keys = [k for k, v in self.children.items() if v.V == max_value]            
            action = choice(max_keys)
            reward = self.children[action].observe(action)

        total = (self.N * self.V) + reward
        self.N += 1
        self.V = total / self.N
        return reward


    
    def observe(self, action):
        # Gets observation based on action
        self.problem.set_action(action)
        self.problem.get_observation()
        self.problem.get_reward()
        observation = self.problem.observation
        reward = None

        if observation in self.children:
            # If observation has been seen previously seen perform selection from there
            reward = self.children[observation].select(self.N)
        else:
            # If it is the first observation perform a 
            self.children[observation] = Node(self.problem, tier=0) # Obtain first observation
            reward = self.children[observation].rollout()
        
        total = (self.N * self.V) + reward
        self.N += 1
        self.V = total / self.N
        return reward
        


    def rollout(self):
        self.N = 1
        self.V = self.problem.rollout()
        self.problem.restart()
        return(self.V)

        
    def add_children(self):
        for action in self.problem.all_actions():
            self.children[action] = Node(self.problem, tier=1)

        

    def print_tree(self):

        if len(self.children) > 0:
            for k, v in self.children.items():
                print(k)
                v.print_tree()


