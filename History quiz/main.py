import tkinter
from tkinter import *
from random import choice


NUMBER_OF_QUESTIONS = 8
questionIndex = 0
choice = -1

questionsArray = ["When did WWI began?",
                  "When did WWII began?",
                  "Who was the first human in space?",
                  "What was the most powerful nuclear weapon ever tested?",
                  "What was the largest air battle in history?",
                  "What was the largest tank battles in history?",
                  "What was the the deadliest battle in history?",
                  "What was the the most successful fighter pilot of all time?"]
answersArray = [[("28/07/1914", 0), ("01/09/1939", 1), ("32/01/1914", 2), ("25/05/1951", 3)],
                [("22/06/1942", 0), ("07/12/1941", 1), ("01/09/1939", 2), ("05/07/1943", 3)],
                [("Buzz Aldrin", 0), ("Alan Shepard", 1), ("Gherman Titov", 2), ("Yuri Gagarin", 3)],
                [("Little Boy by USA", 0), ("Fat man by USA", 1), ("Tsar Bomba by USSR", 2),
                 ("Operation Smiling Buddha by India", 3)],
                [("Battle of midway", 0), ("Battle of Kursk", 1), ("Battle of stalingrad", 2),
                 ("Battle of Britain", 3)],
                [("Battle of midway", 0), ("Battle of Kursk", 1), ("Battle of stalingrad", 2),
                 ("Battle of Britain", 3)],
                [("Battle of Stalingrad", 0), ("Battle of verdun", 1), ("Normandy landings", 2),
                 ("Battle of Iwo Jima", 3)],
                [("Richard Bong USA", 0), ("Tetsuzō Iwamoto Japan Empire", 1), ("Ivan Kozhedub USSR", 2),
                 ("Erich Hartmann Nazi Germany", 3)]]
answersSolutionArray = [0, 2, 3, 2, 1, 1, 0, 3]


# --------------------------- CHECK ANSWER ----------------------------#
def check_answer():
    global questionIndex
    if answersSolutionArray[questionIndex] == choice:
        answer_result_label.config(text="Right answer!", fg="#0f0")
        questionIndex = questionIndex + 1
        if questionIndex == NUMBER_OF_QUESTIONS:
            print("You WON!")
            exit()
        display_question_and_answers(questionIndex, radioButton1, radioButton2, radioButton3, radioButton4,
                                     question_label)
        v.set(-1)

    else:
        answer_result_label.config(text="Wrong answer!", fg="#f00")


# ----------------------------------------------------------------------

# ---------------------------- DISPLAY QUESTIONS AND ANSWERS ------------------------------- #
def display_question_and_answers(index, radioButton1, radioButton2, radioButton3, radioButton4, question_label):
    question_label.config(text=f"{index + 1}. {questionsArray[index]}")
    radioButton1.config(text=answersArray[index][0][0])
    radioButton2.config(text=answersArray[index][1][0])
    radioButton3.config(text=answersArray[index][2][0])
    radioButton4.config(text=answersArray[index][3][0])


def ShowChoice():
    global choice
    choice = v.get()


window = Tk()
window.title("Historical Quiz")
window.config(padx=50, pady=10)
# window.geometry("600x600")

canvas = Canvas(height=300, width=700)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(360, 150, image=logo_image)
canvas.grid(row=0, column=0)

answer_question_button = Button(text="Submit Answer", width=15, command=check_answer)
answer_question_button.grid(row=5, column=2)
answer_result_label = Label(text="")
answer_result_label.grid(row=1, column=2)

question_label = Label(text="")
question_label.config(width=50, height=5, anchor="w")
question_label.grid(row=1, column=0)

# ============================= Radio Buttons ==========================================
v = tkinter.IntVar()
v.set(-1)  # initializing the choice, i.e. Python
radioButton1 = tkinter.Radiobutton(window,
                                   text="answer",
                                   padx=0,
                                   variable=v,
                                   command=ShowChoice,
                                   value=0)
radioButton1.grid(row=2, column=0)

radioButton2 = tkinter.Radiobutton(window,
                                   text="answer",
                                   padx=0,
                                   variable=v,
                                   command=ShowChoice,
                                   value=1)
radioButton2.grid(row=3, column=0)

radioButton3 = tkinter.Radiobutton(window,
                                   text="answer",
                                   padx=0,
                                   variable=v,
                                   command=ShowChoice,
                                   value=2)
radioButton3.grid(row=4, column=0)

radioButton4 = tkinter.Radiobutton(window,
                                   text="answer",
                                   padx=0,
                                   variable=v,
                                   command=ShowChoice,
                                   value=3)
radioButton4.grid(row=5, column=0)
# ============================================================================
display_question_and_answers(questionIndex, radioButton1, radioButton2, radioButton3, radioButton4, question_label)

window.resizable(width=False, height=False)
window.mainloop()
