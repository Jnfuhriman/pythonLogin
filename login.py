import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.title('Login')
tk.Label(window, text='Username').grid(row=0)
tk.Label(window, text='Password').grid(row=1)

username = tk.Entry(window)
password = tk.Entry(window)

username.grid(row=0, column=1)
password.grid(row=1, column=1)

window.mainloop()