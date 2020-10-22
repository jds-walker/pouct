from random import choice

class Node:

    def __init__(self, data, tier=1):
        self.data = data
        self.N = 0 # visitation count
        self.V = 0 # score of state
        self.children = dict()
        self.tier = tier # 1 . Action 0 . Observation

    def _select(self):
        if len(self.children) == 0:
            self.add_children()
        else:
            max_key = max(self.children, key=lambda n:  self.children[n].V)
            max_value = self.children[max_key].V
            max_keys = [k for k, v in self.children.items() if v.V == max_value]            
            self.children[choice(max_keys)]._select()


    def add_children(self):
        if len(self.children) > 0:
            for v in self.children.values():
                v.add_children()
        else: 
            self.children = {"Open-Left": Node(self.data + "a"), "Open-Right": Node(self.data + "b"), "Listen": Node(self.data + "c")}

    def print_tree(self):
        print(self.data)
        if len(self.children) > 0:
            for v in self.children.values():
                v.print_tree()


