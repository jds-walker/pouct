from node import Node
from tiger import TigerProblem, Action
from particle import Particle
from random import choice
from collections import Counter


if __name__ == "__main__":

    while True:
        #Particles
        B = [Particle().state for _ in range(100)]
        
        # #Real Problem
        real = TigerProblem()
        real.get_state()
        print(real.state)
        real.action = Action.LISTEN
        print(real.action)
        real.get_observation()

        # #Sampling from particles
        newB = []
        while len(newB) < 100:
            s = choice(B)
            G = TigerProblem()
            G.state = s
            G.action = real.action
            G.get_observation()
            
            if G.observation == real.observation:
                newB.append(G.state)        
        
        print(Counter(newB))
        break

    while False:
        tiger = TigerProblem()
        
        tree = Node(tiger)
        # tree.B = [Particle().state for _ in range(100)]
        
        # Train
        for _ in range(1000):
            tree.problem.restart()
            tree.select(tree.N)

        # Plan -> Execute -> Plan -> Execute ((s,a,o), (s,a,o)) -
        #     Enumeration first - see the evolution of the beliefs 
        #     after this works scale up
        #         e.g. prticle representation

        # Test
        rewards = []
        for _ in range(1000):
            tree.problem.restart()
            rewards.append(tree.play())
        
        print(sum(rewards)/len(rewards))
        print(rewards[:100])
        break

