from MDP.policy_functions import *


class QuizGame:
    def __init__(self):
        self.STATES = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10", "END"]
        self.ACTIONS = ["quit_game", "play"]

    # return the probability to move from state s to s_next by using action a
    def probability(self, s, a, s_next):
        if a == "quit_game":
            return 1

        elif s_next == "END":
            pass

        
