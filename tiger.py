from numpy.random import choice
from enum import Enum, auto

class State(Enum):
    TIGERLEFT = auto()
    TIGERRIGHT = auto()

    @classmethod
    def get_state(cls):
        return choice([State.TIGERLEFT, State.TIGERRIGHT])
    
class Action(Enum):
    OPENLEFT = auto()
    LISTEN = auto()
    OPENRIGHT = auto()

    @classmethod
    def get_action(cls):
        return choice([Action.OPENLEFT, Action.LISTEN, Action.OPENRIGHT])

    @classmethod
    def all_actions(cls):
        return [Action.OPENLEFT, Action.LISTEN, Action.OPENRIGHT]

class Observation(Enum):
    GROWLLEFT = auto()
    GROWLRIGHT = auto()
    TIGERRIGHT = auto()
    TIGERLEFT = auto()

class Reward(Enum):
    LISTEN = -1
    CORRECT = 10
    INCORRECT = -100


class TigerProblem:

    action = None
    observation = None
    terminal = False

    def __init__(self):
        self.state = State.get_state()

    def get_state(self):
        self.state = State.get_state()

    def get_action(self):
        self.action = Action.get_action()
    
    def all_actions(self):
        return Action.all_actions()

    def get_observation(self):
        if self.action == None:
            raise RuntimeError("Actions should not be null")
        if self.state == State.TIGERRIGHT:
            if self.action == Action.LISTEN:
                self.observation = choice([Observation.GROWLRIGHT, Observation.GROWLLEFT], 1, [0.85, 0.15])[0]
            if (self.action == Action.OPENRIGHT) or (self.action  == Action.OPENLEFT):
                self.observation = Observation.TIGERRIGHT
        if self.state == State.TIGERLEFT:
            if self.action == Action.LISTEN:
                self.observation = choice([Observation.GROWLRIGHT, Observation.GROWLLEFT], 1, [0.15, 0.85])[0]
            if self.action == Action.OPENRIGHT or self.action  == Action.OPENLEFT:
                self.observation = Observation.TIGERLEFT

    def get_reward(self):
        if self.action == Action.LISTEN:
            self.reward = Reward.LISTEN.value
        if self.action == Action.OPENRIGHT:
            self.terminal  = True
            if self.state == State.TIGERRIGHT:
                self.reward = Reward.INCORRECT.value
            else: self.reward = Reward.CORRECT.value
        if self.action == Action.OPENLEFT:
            self.terminal = True
            if self.state == State.TIGERLEFT:
                self.reward = Reward.INCORRECT.value
            else: self.reward = Reward.CORRECT.value

            

