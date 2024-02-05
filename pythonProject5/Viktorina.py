import tkinter as tk
from tkinter import messagebox

class SovietHistoryQuiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Викторина по истории СССР")
        self.master.geometry('1500x1000')

        self.questions = [
            "1. Кто был лидером Октябрьской революции в 1917 году? (псевдоним)",
            "2. Назовите фамилию первого космонавта из СССР.",
            "3. В каком году началась Великая Отечественная война?",
            "4. Назовите фамилию автора термина 'Перестройка'?",
            "5. Какое событие произошло в СССР в 1956 году?",
            "6. Назовите фамилию последнего лидера СССР.",
            "7. Какое имя носил советский мультяшный персонаж с большими ушами?",
            "8. Как назывался первый в мире искусственный спутник земли?",
            "9. Назовите псевдоним человека, при котором произошло больше всего репрессий.",
            "10. Назовите фамилию лидера страны, который подписал с Горбачевым договор, послуживший к окончанию холодной войны?"
        ]

        self.answers = [
            "Ленин",
            "Гагарин",
            "1941",
            "Горбачев",
            "Восстание в Венгрии",
            "Горбачев",
            "Чебурашка",
            "Спутник 1",
            "Сталин",
            "Рейган"
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(master, text=self.questions[self.current_question], wraplength=1400, justify="center", font=('Helvetica', 30))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(master, font=('Helvetica', 40))
        self.answer_entry.pack(pady=20)

        self.submit_button = tk.Button(master, text="Ответить", command=self.check_answer, font=('Helvetica', 30))
        self.submit_button.pack(pady=20)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        correct_answer = self.answers[self.current_question]

        if user_answer.lower() == correct_answer.lower():
            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question])
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Результат", f"Ваш результат: {self.score} из {len(self.questions)}")
            self.master.destroy()

root = tk.Tk()

quiz = SovietHistoryQuiz(root)

root.mainloop()
