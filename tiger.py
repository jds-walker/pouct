from numpy.random import choice, seed
from enum import Enum, auto

seed(42)

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

    def __init__(self):
        self.state = State.get_state()
        self.action = None
        self.observation = None
        self.reward = 0
        self.terminal = False

    def get_state(self):
        self.state = State.get_state()

    def get_action(self):
        if self.terminal == True:
            raise RuntimeError("Should not get action for terminal case")
        self.action = Action.get_action()

    def set_action(self, action):
        if self.terminal == True:
            raise RuntimeError("Should not set action for terminal case")
        self.action = action 
    
    def all_actions(self):
        return Action.all_actions()

    def restart(self):
        self.action = None
        self.observation = None
        self.reward = 0
        self.terminal = False
        self.get_state()

    def rollout(self):
        while self.terminal == False:
            self.get_action()
            self.get_observation()
            self.get_reward()
        return(self.reward)

    def get_observation(self):
        if self.action == None:
            raise RuntimeError("Actions should not be null")
        if self.terminal == True:
            raise RuntimeError("Should not get observation for terminal case")
        if self.state == State.TIGERRIGHT:
            if self.action == Action.LISTEN:
                self.observation = choice([Observation.GROWLRIGHT, Observation.GROWLLEFT], 1, p=[0.85, 0.15])[0]
            if (self.action == Action.OPENRIGHT) or (self.action  == Action.OPENLEFT):
                self.observation = Observation.TIGERRIGHT
        if self.state == State.TIGERLEFT:
            if self.action == Action.LISTEN:
                self.observation = choice([Observation.GROWLRIGHT, Observation.GROWLLEFT], 1, p=[0.15, 0.85])[0]
            if self.action == Action.OPENRIGHT or self.action  == Action.OPENLEFT:
                self.observation = Observation.TIGERLEFT

    def get_reward(self):
        if self.action == Action.LISTEN:
            self.reward += Reward.LISTEN.value
        if self.action == Action.OPENRIGHT:
            self.terminal  = True
            if self.state == State.TIGERRIGHT:
                self.reward += Reward.INCORRECT.value
            else: self.reward += Reward.CORRECT.value
        if self.action == Action.OPENLEFT:
            self.terminal = True
            if self.state == State.TIGERLEFT:
                self.reward += Reward.INCORRECT.value
            else: self.reward += Reward.CORRECT.value

            

