from MDP.policy_functions import *
from MDP.game_params import *

print("\n====================== MDP START ======================")
quiz = QuizGame()

policy = get_policy(quiz.STATES, quiz.ACTIONS, probability, reward)

print("\n====================== Policy has been found! ======================\n")
print(policy)
