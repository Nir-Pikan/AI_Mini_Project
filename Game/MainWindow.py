from tkinter import Tk, Label, Button
import random


class GUIManager:
    def __init__(self, master):
        self.master = master
        self.questionNumber = 1
        self.totalReward = 0
        self.rewards = [1, 5, 20, 50, 100, 500, 1000, 5000, 15000, 75000]
        self.probabilities = [0.99, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]

        master.title("Quiz Simulator")
        master.config(padx=50, pady=10)

        self.questionNumberLabel = Label(master, text=f"Question number: {self.questionNumber}")
        self.questionNumberLabel.grid(row=0, column=0)

        self.rightAnswerProbabilityLabel = Label(master, text=f"{self.probabilities[self.questionNumber-1]}")
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

    def calculateChance(self):
        chance = random.random()
        print(chance)  # delete later
        print(self.probabilities[self.questionNumber-1])  # delete later

        if chance < (self.probabilities[self.questionNumber-1]):
            self.totalReward = self.totalReward + self.rewards[self.questionNumber - 1]
            self.totalRewardLabel.config(text=f"Total Reword: {self.totalReward}")
            print(self.totalReward)
            self.questionNumber = self.questionNumber + 1
            self.rightAnswerProbabilityLabel.config(text=f"{self.probabilities[self.questionNumber - 1]}")
            self.questionNumberLabel.config(text=f"Question number: {self.questionNumber}")

            if self.questionNumber > 10:
                self.gameFinished()
        else:
            print("Game Over")
            self.gameStatusLabel.config(text="Game Over",fg='#f00')
            self.answerButton.config(state="disabled")
            self.quitButton.config(state="disable")

    def quit(self):
        self.gameStatusLabel.config(text="You Quit!", fg="#0f0")
        self.answerButton.config(state="disabled")
        self.quitButton.config(state="disable")

    def gameRestart(self):
        self.questionNumber = 1
        self.totalReward = 0
        self.questionNumberLabel.config(text=f"Question number: {self.questionNumber}")
        self.totalRewardLabel.config(text=f"Total Reword: {self.totalReward}")
        self.rightAnswerProbabilityLabel.config(text=f"{self.probabilities[self.questionNumber-1]}")
        self.gameStatusLabel.config(text="")
        self.answerButton.config(state="active")
        self.quitButton.config(state="active")

    def gameFinished(self):
        self.gameStatusLabel.config(text="Winner!", fg="#0f0")
        self.answerButton.config(state="disabled")
        self.quitButton.config(state="disable")
