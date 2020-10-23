from abc import ABC, abstractmethod

class POMDP(ABC):

    @abstractmethod
    def get_actions(self):
        """Return possible actions from current state"""
        return set()

    @abstractmethod
    def get_observation(self, state, action):
        """Return an observation based on state and action"""
        return set()

    @abstractmethod
    def is_terminal(self):
        """Return true if there are no further actions"""
        return True



    #             0                                 :Reward gets averaged here
    #       /     |       \
#     # open left  Listen  Open Right               :Actions (reward gets averaged here)

#        /\          |            /\
    # TL  TR         /\          TL TR              :Observations (reward gets averaged here)    
    #               GR GL     
#   -100 +10       -1   -1      +10 -100            :Rewards
    # terminal                    terminal
                #   |    |   
                #   0
                    
