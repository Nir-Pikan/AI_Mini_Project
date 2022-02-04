from MDP.policy_functions import *
from MDP.game_params import *

print("start\n")
quiz = QuizGame()

policy = policy_iteration(quiz.STATES, quiz.ACTIONS, quiz.probability, quiz.reward)

print("\n====================== Policy has been found! ======================\n")
print(policy)
