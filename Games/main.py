import tkinter as tk  
from tkinter import Toplevel  
from Games.gamewuzi import GomokuGame  
from Games.mathquiz import MathQuizApp  
from Games.game2048 import Game2048  

def open_games(root):  
    # 创建新的游戏合集窗口  
    game_window = Toplevel(root)  # 新窗口  
    game_window.title("小游戏合集")  
    game_window.geometry("800x400")  
    game_window.configure(bg="#f7f9fc")  # 设置背景颜色
    font = ('Arial', 20, 'bold')  
    font_16 = ('Arial', 16)
    # 标题标签  
    title_label = tk.Label(  
        game_window,   
        text="小游戏合集",   
        font=('Arial', 24, 'bold'),   
        bg="#f7f9fc",   
        fg="#34495e"  
    )  
    title_label.pack(pady=20)  

    # 按钮点击事件  
    def open_gomoku():  
        gomoku_window = Toplevel(game_window)  
        gomoku_window.title("五子棋")  
        GomokuGame(gomoku_window)
    def open_mathquiz():  
        mathquiz_window = Toplevel(game_window)  
        mathquiz_window.title("数学 Quiz")  
        MathQuizApp(mathquiz_window)
    def open_2048():  
        game2048_window = Toplevel(game_window)  
        game2048_window.title("2048")  
        Game2048(game2048_window)  

    # 创建一个按钮框架用于排列按钮  
    button_frame = tk.Frame(game_window, bg="#f7f9fc")  
    button_frame.pack(pady=30)  

    # 按钮样式  
    button_style = {  
        "width": 15,  
        "height": 2,  
        "font": font_16,  
        "bg": "#3498db",  
        "fg": "white",  
        "relief": tk.RAISED,  
        "bd": 3  
    }  

    # 添加按钮  
    button_gomoku = tk.Button(  
        button_frame,   
        text="五子棋",   
        command=open_gomoku,   
        **button_style  
    )  
    button_math = tk.Button(  
        button_frame,   
        text="数学 Quiz",   
        command=open_mathquiz,   
        **button_style  
    )  
    button_2048 = tk.Button(  
        button_frame,   
        text="2048",   
        command=open_2048,   
        **button_style  
    )  

    # 按钮网格布局  
    button_gomoku.grid(row=0, column=0, padx=20, pady=10)  
    button_math.grid(row=0, column=1, padx=20, pady=10)  
    button_2048.grid(row=0, column=2, padx=20, pady=10)  

