from random import choice
from math import sqrt
from enum import Enum
from tiger import TigerProblem


class Node:

    def __init__(self, problem: TigerProblem, exploration = 7, tier=1):
        self.problem = problem
        self.N = 0 # visitation count
        self.total = 0
        self.V = 0 # score of state
        self.children = dict()
        self.tier = tier # 1 . Action 0 . Observation
        self.exploration = exploration
        self.B = 0 # Belief
    
    def belief(self):
        # B(s, h) = Pr(st = s | ht = h). 
        # The belief state is the probability distribution over states given history h 
        pass

    def select(self, totalN):
        reward = None
        choice_value = None
        if len(self.children) == 0:
            #rollout
            self.add_children()
            random_action = choice(list(self.children.keys()))
            reward = self.children[random_action].observe(random_action)

        else:       
            minimum_rollouts = min(self.children, key=lambda n: self.children[n].N)            
            minimum_value = self.children[minimum_rollouts].N           
            if (minimum_value>0):               
                choice_key = max(self.children, key=lambda n:  self.children[n].V + ((self.exploration * sqrt(totalN/self.children[n].N)) ))               
                choice_value = self.children[choice_key].V          
            else:              
                choice_key = minimum_rollouts                
                choice_value = self.children[choice_key].V   

            choice_keys = [k for k, v in self.children.items() if v.V == choice_value] 
            action = choice(choice_keys)
            reward = self.children[action].observe(action)

        self.total += reward
        self.N += 1
        self.V = self.total / self.N
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
            if self.problem.terminal == True:
                self.total += self.problem.reward
                self.N += 1
                self.V = self.total / self.N
                return self.problem.reward
            reward = self.children[observation].select(self.N)
        else:
            # If it is the first observation perform a 
            self.children[observation] = Node(self.problem, tier=0) # Obtain first observation
            if self.problem.terminal == True:
                self.total += self.problem.reward
                self.N += 1
                self.V = self.total / self.N
                return self.problem.reward

            reward = self.children[observation].rollout()
        
        self.total += reward
        self.N += 1
        self.V = self.total / self.N
        return reward
        
    def rollout(self):
        self.N = 1
        self.V = self.problem.rollout()
        return(self.V)

    def add_children(self):
        for action in self.problem.all_actions():
            self.children[action] = Node(self.problem, tier=1)

    def play(self):
        optimal = max(self.children, key=lambda n: self.children[n].N)    
        self.problem.set_action(optimal)        
        self.problem.get_observation()
        self.problem.get_reward()
        if self.problem.terminal == False:
            return self.children[optimal].children[self.problem.observation].play()
        else: 
            return self.problem.reward


