POSSIBLE_TRANSITIONS_DICT = {
    ("Q1", "Q2"): (0.99, 1),
    ("Q2", "Q3"): (0.9, 5),
    ("Q3", "Q4"): (0.8, 10),
    ("Q4", "Q5"): (0.7, 50),
    ("Q5", "Q6"): (0.6, 100),
    ("Q6", "Q7"): (0.5, 500),
    ("Q7", "Q8"): (0.4, 1000),
    ("Q8", "Q9"): (0.3, 5000),
    ("Q9", "Q10"): (0.2, 15000),
    ("Q10", "END"): (0.1, 75000),
}

PROBABILITY_AND_REWARD_DICT = {
    "Q1": (0.99, 1),
    "Q2": (0.9, 5),
    "Q3": (0.8, 10),
    "Q4": (0.7, 50),
    "Q5": (0.6, 100),
    "Q6": (0.5, 500),
    "Q7": (0.4, 1000),
    "Q8": (0.3, 5000),
    "Q9": (0.2, 15000),
    "Q10": (0.1, 75000),
}


# return the probability to move from state s to next_s by using action a
def probability(s, a, next_s):

    # chose to quit
    if a == "quit_game" and next_s == "END":
        return 1

    # impossible
    elif a == "quit_game" and next_s != "END":
        return 0

    # chose to play and win
    elif (s, next_s) in POSSIBLE_TRANSITIONS_DICT:
        p, r = PROBABILITY_AND_REWARD_DICT[s]
        return p

    # chose to play and lose
    elif next_s == "END":
        p, r = PROBABILITY_AND_REWARD_DICT[s]
        return 1. - p

    # unrealistic transitions
    else:
        return 0


# return the reward for doing action a from state s and reaching state next_s
def reward(s, a, next_s):

    # chose to quit
    if a == "quit_game":
        return 0

    # correct answer
    elif (s, next_s) in POSSIBLE_TRANSITIONS_DICT:
        p, r = PROBABILITY_AND_REWARD_DICT[s]
        return r

    # wrong answer
    else:
        reward_sum = 0
        temp = int(s.replace("Q", ""))
        for index in range(1, temp):
            s_index = "Q" + str(index)
            p, r = PROBABILITY_AND_REWARD_DICT[s_index]

            reward_sum += r
        return -reward_sum


class QuizGame:
    def __init__(self):
        self.STATES = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10", "END"]
        self.ACTIONS = ["quit_game", "play"]
