from tkinter import Tk

from Game.MainWindow import GUIManager


def startGame(policy):
    root = Tk()
    GUIManager(root, policy)
    root.mainloop()
