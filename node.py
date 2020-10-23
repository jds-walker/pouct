from random import choice
from enum import Enum

class Node:

    def __init__(self, data, tier=1):
        self.data = data
        self.N = 0 # visitation count
        self.V = 0 # score of state
        self.children = dict()
        self.tier = tier # 1 . Action 0 . Observation

    def select(self):
        if len(self.children) == 0:
            print(self.data)
            return self
        else:
            max_key = max(self.children, key=lambda n:  self.children[n].V)
            max_value = self.children[max_key].V
            max_keys = [k for k, v in self.children.items() if v.V == max_value]            
            self.children[choice(max_keys)].select()

    def add_children(self, children):
        for child in children:
            self.children[child] = Node(self.data + ", " + str(child))

    def print_tree(self):
        print(self.data)
        if len(self.children) > 0:
            for v in self.children.values():
                v.print_tree()


