import Game.main
from MDP.policy_functions import *
from MDP.game_params import *


def main():
    print("\n====================== MDP START ======================")
    quiz = QuizGame()

    policy = get_policy(quiz.STATES, quiz.ACTIONS, probability, reward)
    print("\n====================== Policy has been found! ======================\n")
    print(policy)
    Game.main.startGame(policy)


if __name__ == "__main__":
    main()
