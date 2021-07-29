import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
font = ("Ariel", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        # Window
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg='#375362')
        # canvas
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=font)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.false = tkinter.PhotoImage(file="images/false.png")
        self.true = tkinter.PhotoImage(file="images/true.png")
        self.false_button = tkinter.Button(image=self.false, highlightthickness=0, command=self.false_press)
        self.false_button.grid(column=1, row=2)
        self.true_button = tkinter.Button(image=self.true, highlightthickness=0, command=self.true_press)
        self.true_button.grid(column=0, row=2, )
        self.web_label = tkinter.Label(text=f"Score:{self.score}", fg="white", bg="#375362")
        self.web_label.grid(column=1, row=0)
        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You reach end of question")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")


    def false_press(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def true_press(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
            self.web_label.config(text=f"Score:{self.score}")
        else:
            self.canvas.config(bg="red")


        self.window.after(1000, self.get_next_question)

