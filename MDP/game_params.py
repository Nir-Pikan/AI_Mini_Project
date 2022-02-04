import random

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


class QuizGame:
    def __init__(self):
        self.STATES = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10", "END"]
        self.ACTIONS = ["quit_game", "play"]

    # return the probability to move from state s to s_next by using action a
    def probability(self, s, a, s_next):

        # chose to quit
        if a == "quit_game" and s_next == "END":
            return 1

        # impossible
        elif a == "quit_game" and s_next != "END":
            return 0

        # chose to play and won
        elif (s, s_next) in POSSIBLE_TRANSITIONS_DICT:
            p, r = PROBABILITY_AND_REWARD_DICT[s]
            return p

        # chose to play and lose
        elif s_next == "END":
            p, r = PROBABILITY_AND_REWARD_DICT[s]
            return 1 - p

        # unrealistic transitions
        else:
            return 0

    # return the reward for doing action a from state s
    def reward(self, s, a):

        # chose to quit
        if a == "quit_game":
            return 0

        else:
            rand = random.randint(0, 100)
            p, r = PROBABILITY_AND_REWARD_DICT[s]

            # answered correct
            if rand < p * 100:
                return r

            # answered wrong
            else:
                match s:
                    case "Q1":
                        return 0
                    case "Q2":
                        return -1
                    case "Q3":
                        return -6
                    case "Q4":
                        return -16
                    case "Q5":
                        return -66
                    case "Q6":
                        return -166
                    case "Q7":
                        return -666
                    case "Q8":
                        return -1666
                    case "Q9":
                        return -6666
                    case "Q10":
                        return -21666

# print("start\n")
# quiz = QuizGame()
# print(quiz.STATES)
# print(quiz.ACTIONS)
# print(probability(quiz.STATES[0], quiz.ACTIONS[0], quiz.STATES[10]))
# print(probability(quiz.STATES[0], quiz.ACTIONS[1], quiz.STATES[10]))
# print(probability(quiz.STATES[1], quiz.ACTIONS[0], quiz.STATES[5]))
# print(probability(quiz.STATES[5], quiz.ACTIONS[0], quiz.STATES[6]))
# print(probability(quiz.STATES[5], quiz.ACTIONS[1], quiz.STATES[6]))
# print(probability(quiz.STATES[5], quiz.ACTIONS[1], quiz.STATES[7]))
#
# for i in range(0, 10):
#     print(reward(quiz.STATES[8], quiz.ACTIONS[1]))
