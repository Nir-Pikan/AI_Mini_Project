from tkinter import Tk, Label, Button
import random


class GUIManager:
    def __init__(self, master, policy):
        self.policy = policy
        self.master = master
        self.questionNumber = 1
        self.totalReward = 0
        self.rewards = [1, 5, 10, 50, 100, 500, 1000, 5000, 15000, 75000]
        self.probabilities = [0.99, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]

        master.title("Quiz Simulator")
        master.config(padx=50, pady=10)

        self.questionNumberLabel = Label(master, text=f"Question number: {self.questionNumber}")
        self.questionNumberLabel.grid(row=0, column=0)

        self.rightAnswerProbabilityLabel = Label(master, text=f"{self.probabilities[self.questionNumber - 1]}")
        self.rightAnswerProbabilityLabel.grid(row=0, column=1)

        self.totalRewardLabel = Label(master, text=f"Total Reword: {self.totalReward}")
        self.totalRewardLabel.grid(row=1, column=1)

        self.gameStatusLabel = Label(master, text="")
        self.gameStatusLabel.grid(row=2, column=1)

        self.answerButton = Button(master, text="Answer", command=self.calculateChance)
        self.answerButton.grid(row=1, column=0)

        self.quitButton = Button(master, text="Quit", command=self.quit)
        self.quitButton.grid(row=2, column=0)

        self.restartButton = Button(master, text="Restart", command=self.gameRestart)
        self.restartButton.grid(row=3, column=0)

        self.adviceLabel = Label(master, text="")
        self.getMDPAdvice()  # set the adviceLabel with MDP result
        self.adviceLabel.grid(row=3, column=1)

    def calculateChance(self):
        chance = random.random()
        print(f"Chance for correct answer: {self.probabilities[self.questionNumber - 1]}")
        print(f"The random value is: {chance}")
        self.getMDPAdvice()
        if chance < (self.probabilities[self.questionNumber - 1]):
            self.totalReward = self.totalReward + self.rewards[self.questionNumber - 1]
            self.totalRewardLabel.config(text=f"Total Reword: {self.totalReward}")
            print(f"Total reward: {self.totalReward}")
            self.questionNumber = self.questionNumber + 1
            self.rightAnswerProbabilityLabel.config(text=f"{self.probabilities[self.questionNumber - 1]}")
            self.questionNumberLabel.config(text=f"Question number: {self.questionNumber}")

            if self.questionNumber > 10:
                self.gameFinished()
        else:
            print("Game Over")
            self.gameStatusLabel.config(text="Game Over", fg='#f00')
            self.answerButton.config(state="disabled")
            self.quitButton.config(state="disable")
            self.totalRewardLabel.config(text=f"Total Reword: 0")
            self.adviceLabel.config(text="")

    def quit(self):
        self.gameStatusLabel.config(text="You Quit!", fg="#0f0")
        self.answerButton.config(state="disabled")
        self.quitButton.config(state="disable")
        self.adviceLabel.config(text="")

    def gameRestart(self):
        self.questionNumber = 1
        self.totalReward = 0
        self.questionNumberLabel.config(text=f"Question number: {self.questionNumber}")
        self.totalRewardLabel.config(text=f"Total Reword: {self.totalReward}")
        self.rightAnswerProbabilityLabel.config(text=f"{self.probabilities[self.questionNumber - 1]}")
        self.gameStatusLabel.config(text="")
        self.answerButton.config(state="active")
        self.quitButton.config(state="active")
        self.getMDPAdvice()

    def gameFinished(self):
        self.gameStatusLabel.config(text="Winner!", fg="#0f0")
        self.answerButton.config(state="disabled")
        self.quitButton.config(state="disable")

    def getMDPAdvice(self):
        if self.policy["Q" + str(self.questionNumber)] == "play":
        # if self.questionNumber < 3:

            self.adviceLabel.config(text="Policy: play 😉", fg='#0f0')
        else:
            self.adviceLabel.config(text="Policy: stop!", fg='#f00')
