import tkinter as tk
import math
from Games.mathquiz import MathQuizApp
from Games.gamewuzi import GomokuGame
from Games.game2048 import Game2048

root = tk.Tk()
root.title('计算器')
# 界面大小
root.geometry('500x500')

root.attributes("-alpha", 0.9)
# root["background"] = "#ffffff"
font = ('Arial', 20)
font_16 = ('Arial', 16)
result_num = tk.StringVar()
# result_num.set('0')

tk.Label(root,
         textvariable=result_num, font=font, height=2,
         width=20, justify=tk.LEFT, anchor=tk.SE
         ).grid(row=1, column=1, columnspan=4)

button_pow = tk.Button(root, text='^', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_lg = tk.Button(root, text='lg', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_ln = tk.Button(root, text='ln', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_lb = tk.Button(root, text='(', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_rb = tk.Button(root, text=')', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_pow.grid(row=2, column=1, padx=2, pady=2)
button_lg.grid(row=2, column=2, padx=2, pady=2)
button_ln.grid(row=2, column=3, padx=2, pady=2)
button_lb.grid(row=2, column=4, padx=2, pady=2)
button_rb.grid(row=2, column=5, padx=2, pady=2)

button_sqrt = tk.Button(root, text='√', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_clear = tk.Button(root, text='C', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_back = tk.Button(root, text='←', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_division = tk.Button(root, text='/', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_mult = tk.Button(root, text='x', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_sqrt.grid(row=3, column=1, padx=2, pady=2)
button_clear.grid(row=3, column=2, padx=2, pady=2)
button_back.grid(row=3, column=3, padx=2, pady=2)
button_division.grid(row=3, column=4, pady=2)
button_mult.grid(row=3, column=5, padx=2, pady=2)

button_factorial = tk.Button(root, text='!', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_seven = tk.Button(root, text='7', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_eight = tk.Button(root, text='8', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_nine = tk.Button(root, text='9', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_sub = tk.Button(root, text='-', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_factorial.grid(row=4, column=1, padx=2, pady=2)
button_seven.grid(row=4, column=2, padx=2, pady=2)
button_eight.grid(row=4, column=3, padx=2, pady=2)
button_nine.grid(row=4, column=4, padx=2, pady=2)
button_sub.grid(row=4, column=5, padx=2, pady=2)

button_diff = tk.Button(root, text='求导', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_four = tk.Button(root, text='4', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_five = tk.Button(root, text='5', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_six = tk.Button(root, text='6', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_add = tk.Button(root, text='+', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_diff.grid(row=5, column=1, padx=2, pady=2)
button_four.grid(row=5, column=2, padx=2, pady=2)
button_five.grid(row=5, column=3, padx=2, pady=2)
button_six.grid(row=5, column=4, pady=2)
button_add.grid(row=5, column=5, padx=2, pady=2)

button_pi = tk.Button(root, text='π', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_one = tk.Button(root, text='1', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_two = tk.Button(root, text='2', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_three = tk.Button(root, text='3', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_mod = tk.Button(root, text='%', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_pi.grid(row=6, column=1, padx=2, pady=2)
button_one.grid(row=6, column=2, padx=2, pady=2)
button_two.grid(row=6, column=3, padx=2, pady=2)
button_three.grid(row=6, column=4, padx=2, pady=2)
button_mod.grid(row=6, column=5, padx=2, pady=2)

button_e = tk.Button(root, text='e', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_zero = tk.Button(root, text='0', width=12, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_dot = tk.Button(root, text='.', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_equal = tk.Button(root, text='=', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_e.grid(row=7, column=1, padx=2, pady=2)
button_zero.grid(row=7, column=2, padx=2, pady=2, columnspan=2)
button_dot.grid(row=7, column=4, pady=2)
button_equal.grid(row=7, column=5, padx=2, pady=2)

button_bar = tk.Button(root, text='柱状图', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_pie = tk.Button(root, text='饼状图', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_equation = tk.Button(root, text='求方程', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_regression = tk.Button(root, text='回归曲线', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')  # 添加回归曲线按钮

button_equation.grid(row=8, column=1, padx=2, pady=2)
button_bar.grid(row=8, column=2, padx=2, pady=2)
button_pie.grid(row=8, column=3, padx=2, pady=2)
button_regression.grid(row=8, column=4, padx=2, pady=2)  # 放置回归曲线按钮到合适位置

# 创建跳转到问答游戏的按钮
button_quiz = tk.Button(root, text='问答游戏', width=10, font=('Arial', 16), relief=tk.FLAT, bg='#b1b2b2')
button_quiz.grid(row=9, column=1, padx=2, pady=2)

# 创建跳转到五子棋游戏的按钮
button_gomoku = tk.Button(root, text='五子棋游戏', width=10, font=('Arial', 16), relief=tk.FLAT, bg='#b1b2b2')
button_gomoku.grid(row=9, column=3, padx=2, pady=2)

# 创建跳转到2048游戏的按钮
button_2048 = tk.Button(root, text='进入2048游戏', width=10, font=('Arial', 16), relief=tk.FLAT, bg='#b1b2b2')
button_2048.grid(row=9, column=5, padx=2, pady=2)

#############点击事件##############
def click_button(x):
    print('x:\t', x)
    result_num.set(result_num.get() + x)


# 计算表达式
def calculation():
    opt_str = result_num.get()
    opt_str = opt_str.replace('e', str(math.e))
    opt_str = opt_str.replace('^', '**')
    opt_str = opt_str.replace('lg(', 'math.log10(')
    opt_str = opt_str.replace('ln(', 'math.log(')
    opt_str = opt_str.replace('√', 'math.sqrt')
    opt_str = opt_str.replace('π', str(math.pi))
    result = eval(opt_str)
    print(opt_str)
    result_num.set(str(result))


# 清屏操作
def clear():
    result_num.set("")


# 退格操作
def back():
    str = result_num.get()
    if (str.find("lg") or str.find("ln")):
        print("找到了")
        str = ""
    else:
        str = str[:len(str) - 1]
    result_num.set(str)


#######点击按钮显示在屏幕上#########
button_one.config(command=lambda: click_button('1'))
button_two.config(command=lambda: click_button('2'))
button_three.config(command=lambda: click_button('3'))
button_four.config(command=lambda: click_button('4'))
button_five.config(command=lambda: click_button('5'))
button_six.config(command=lambda: click_button('6'))
button_seven.config(command=lambda: click_button('7'))
button_eight.config(command=lambda: click_button('8'))
button_nine.config(command=lambda: click_button('9'))
button_zero.config(command=lambda: click_button('0'))
button_add.config(command=lambda: click_button('+'))
button_sub.config(command=lambda: click_button('-'))
button_mult.config(command=lambda: click_button('*'))
button_division.config(command=lambda: click_button('/'))
button_mod.config(command=lambda: click_button('%'))
button_factorial.config(command=lambda: click_button('!'))
button_sqrt.config(command=lambda: click_button('√('))
button_pow.config(command=lambda: click_button('^'))
button_lg.config(command=lambda: click_button('lg('))
button_ln.config(command=lambda: click_button('ln('))
button_lb.config(command=lambda: click_button('('))
button_rb.config(command=lambda: click_button(')'))
button_pi.config(command=lambda: click_button('π'))
button_e.config(command=lambda: click_button('e'))


##########给按钮绑定功能###########
button_equal.config(command=calculation)
button_clear.config(command=clear)
button_back.config(command=back)

"""为数字游戏绑定一个页面跳转"""
def open_math_quiz():
    quiz_window = tk.Toplevel(root)
    app = MathQuizApp(quiz_window)


button_quiz.config(command=open_math_quiz)

"""为五子棋绑定一个页面跳转"""
def open_gomoku_game():
    gomoku_window = tk.Toplevel(root)
    game = GomokuGame(gomoku_window)


button_gomoku.config(command=open_gomoku_game)

"""为2048绑定一个页面跳转"""
def open_2048_game():
    game_2048_window = tk.Toplevel(root)
    game = Game2048(game_2048_window)


button_2048.config(command=open_2048_game)

root.mainloop()