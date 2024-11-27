import tkinter as tk  
from tkinter import PhotoImage, Toplevel  
from Games.main import open_games  

# 主窗口设置  
def main_window():  
    root = tk.Tk()  
    root.title('计算器')  
    root.geometry('800x400')  
    root.configure(bg="#f7f9fc")  # 设置背景颜色  

    # 创建一个跳转按钮  
    button_example = tk.Button(  
        root, text="小游戏", font=("Arial", 16), command=lambda: open_games(root)
    )  
    button_example.pack(pady=20)  
    
    root.mainloop()   

# 启动程序  
if __name__ == '__main__':  
    main_window()