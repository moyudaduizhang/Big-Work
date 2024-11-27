import tkinter as tk
from tkinter import messagebox
import random


class MathQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("数学问答游戏")
        self.difficulty = tk.StringVar(value="简单")  # 默认难度
        self.score = 0
        self.current_streak = 0  # 连击计数
        self.time_limit = 10  # 每道题目时间限制（秒）
        self.timer_id = None  # 计时器标识
        # 难度选择
        self.difficulty_label = tk.Label(master, text="选择难度:", font=("Arial", 16))
        self.difficulty_label.pack(pady=10)

        self.easy_button = tk.Radiobutton(
            master, text="简单", variable=self.difficulty, value="简单", font=("Arial", 14)
        )
        self.medium_button = tk.Radiobutton(
            master, text="中等", variable=self.difficulty, value="中等", font=("Arial", 14)
        )
        self.hard_button = tk.Radiobutton(
            master, text="困难", variable=self.difficulty, value="困难", font=("Arial", 14)
        )

        self.easy_button.pack()
        self.medium_button.pack()
        self.hard_button.pack()

        # 显示问题
        self.question_label = tk.Label(master, text="", font=("Arial", 24))
        self.question_label.pack(pady=20)

        # 用户输入
        self.answer_entry = tk.Entry(master, font=("Arial", 24))
        self.answer_entry.pack(pady=20)

        # 提交按钮
        self.submit_button = tk.Button(
            master, text="提交答案", command=self.check_answer, font=("Arial", 24)
        )
        self.submit_button.pack(pady=20)

        # 显示计时器
        self.timer_label = tk.Label(master, text="", font=("Arial", 20))
        self.timer_label.pack(pady=20)

        # 开始游戏
        self.generate_question()

    def generate_question(self):
        # 根据难度生成随机题目
        if self.difficulty.get() == "简单":
            self.num1 = random.randint(1, 20)
            self.num2 = random.randint(1, 20)
        elif self.difficulty.get() == "中等":
            self.num1 = random.randint(1, 50)
            self.num2 = random.randint(1, 50)
        else:  # 困难
            self.num1 = random.randint(1, 100)
            self.num2 = random.randint(1, 100)

        self.operator = random.choice(['+', '-', '*', '/'])

        if self.operator == '/':
            self.num1 = self.num1 * self.num2  # 确保除法可以整除

        self.question = f"{self.num1} {self.operator} {self.num2}"
        self.question_label.config(text=self.question)

        # 每次生成新问题时重置计时器
        self.reset_timer()

    def reset_timer(self):
        if self.timer_id:  # 如果已有计时器，先取消
            self.master.after_cancel(self.timer_id)
        self.remaining_time = self.time_limit
        self.update_timer()

    def update_timer(self):
        if self.remaining_time > 0:
            self.timer_label.config(text=f"剩余时间: {self.remaining_time} 秒")
            self.remaining_time -= 1
            self.timer_id = self.master.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="时间到！")
            messagebox.showwarning("时间到", "时间到！请尽快回答。")
            self.check_answer()  # 时间到后自动检查答案

    def check_answer(self):
        # 检查用户答案
        try:
            user_answer = float(self.answer_entry.get())
            correct_answer = self.calculate_answer()

            if user_answer == correct_answer:
                self.score += 10  # 每答对一次加10分
                self.current_streak += 1  # 连击加1
                messagebox.showinfo(
                    "正确", f"回答正确！当前得分: {self.score}，连击数: {self.current_streak}"
                )
            else:
                messagebox.showerror(
                    "错误", f"回答错误！正确答案是: {correct_answer} 连击数重置。"
                )
                self.current_streak = 0  # 连击数重置到0

            self.answer_entry.delete(0, tk.END)  # 清空输入框
            self.generate_question()  # 生成下一个题目
        except ValueError:
            messagebox.showerror("输入错误", "请确保输入一个有效的数字。")

    def calculate_answer(self):
        # 计算正确答案
        if self.operator == '+':
            return self.num1 + self.num2
        elif self.operator == '-':
            return self.num1 - self.num2
        elif self.operator == '*':
            return self.num1 * self.num2
        elif self.operator == '/':
            return self.num1 / self.num2


if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
