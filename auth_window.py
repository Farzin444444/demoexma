import tkinter as tk
from tkinter import ttk,messagebox
import pandas as pd
from sqlalchemy import create_engine,text

engine = create_engine('postgresql://postgres:admin@localhost/postgres')
class LoginWindow:
    def __init__(self,root):
        self.window=tk.Tk()
        self.window.title("wwww")
        self.window.geometry("400x400")

        tk.Label(self.window, text="Магазин обувь",font = ("arial",20)).pack(pady=20)
        tk.Label(self.window,text="Логин:").pack()
        self.login = tk.Entry(self.window,width=30)
        self.login.pack(pady=5)
        self.login.pack(pady=5)
        self.password = tk.Entry(self.window,show="*",width=30)
        tk.Button(self.window,text="Войти",command=self.check).pack(pady=5)
        tk.Button(self.window,text="гость",command=self.guest).pack()

        def check(self):
            df = pd.read_sql(f"SELECT * FROM users WHERE Логин='{self.login.get()}' AND Пароль='{self.password.get()}'",
                             engine)
            if len(df) > 0:
                role = df.iloc[0]['Роль сотрудника']
                self.window.destroy()
                MainWindow(role)
            else:
                messagebox.showerror("Ошибка", "Неверный логин или пароль")

        def guest(self):
            self.window.destroy()
            MainWindow("Гость")