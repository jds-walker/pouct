from random import choice
from enum import Enum
from tiger import TigerProblem

class Node:

    def __init__(self, problem: TigerProblem, parent=None, tier=1):
        self.problem = problem
        self.N = 0 # visitation count
        self.V = 0 # score of state
        self.parent = parent
        self.children = dict()
        self.tier = tier # 1 . Action 0 . Observation
        

    def select(self):
        if len(self.children) == 0:
            #rollout
            self.add_children()
            reward = choice(list(self.children.values())).rollout()
            total = (self.N * self.V) + reward
            self.N += 1
            self.V = total / self.N
            return reward
        else:
            # Finds best next action then observe
            max_key = max(self.children, key=lambda n:  self.children[n].V)
            max_value = self.children[max_key].V
            max_keys = [k for k, v in self.children.items() if v.V == max_value]            
            action = choice(max_keys)
            return self.children[action].observe(action)

    
    def observe(self, action):
        # Gets observation based on action
        self.problem.set_action(action)
        self.problem.get_observation()
        self.problem.get_reward()
        observation = self.problem.observation
        if observation in self.children:
            # If observation has been seen previously seen perform selection from there
            reward = self.children[observation].select()
            total = (self.N * self.V) + reward
            self.N += 1
            self.V = total / self.N
            return reward
        else:
            # If it is the first observation perform a 
            print(observation)
            self.children[observation] = Node(self.problem, parent=self, tier=0) # Obtain first observation
            reward = self.children[observation].select()
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
            self.children[action] = Node(self.problem, parent=self, tier=1)
        

    def print_tree(self):

        if len(self.children) > 0:
            for k, v in self.children.items():
                print(k)
                v.print_tree()


