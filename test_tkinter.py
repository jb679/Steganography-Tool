import tkinter as tk

window = tk.Tk()
window.title("Test Window")
window.geometry("300x200")
tk.Label(window, text="Hello, Tkinter!").pack()
window.mainloop()
