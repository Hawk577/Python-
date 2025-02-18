import tkinter as tk 
window = tk.Tk()
window.title("Simple and Compound Interest Calculator")
window.geometry("600x400")
welcome = tk.Label(window, text ='''
                   Welcome to Simple Interest and Compound Interest calculator
                                made by Hawk577
                   ''')
welcome.grid(row = 0, column=0, columnspan=3, pady=10)
P = tk.Label(window, text = "Please enter Principal amount ")
P.grid(row=1, column=0)
window.mainloop()