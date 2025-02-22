import tkinter as tk
window = tk.Tk()
welcome= tk.Label(window,text="Welcome to SI and CI calculator")
creator = tk.Label(window, text = "By Hawk577")
pStatement= tk.Label(window, text="Please enter principal amount: ")
rStatement = tk.Label(window, text="Please enter rate of interest: ")
tStatement = tk.Label(window, text="Please enter time period (in years): ")
result = tk.Label(window, text="")
Error= tk.Label(window, text="")
pEntry =  tk.Entry(window)
rEntry =  tk.Entry(window)
tEntry =  tk.Entry(window)
def si_calculate(pEntry, rEntry, tEntry, Error, result):
    try:
        principal= float(pEntry.get())
        rate= float(pEntry.get())
        time= float(pEntry.get())
        res = (principal*rate*time)/100
        result.config(text=f"Simple Interest is {res}")
    except:
        Error.config(text="Please enter numbers only in the input fields !")
        pEntry.delete(0, tk.END)
        tEntry.delete(0, tk.END)
        rEntry.delete(0, tk.END)
        principal = 0
        time = 0
        rate = 0
def ci_calculate(pEntry, rEntry, tEntry, Error, result):
    try:
        #CI = P*(1+R/100)**T-P
        principal= float(pEntry.get())
        rate= float(pEntry.get())
        time= float(pEntry.get())
        res = (principal*((1+(rate/100))**time)-principal)
        result.config(text=f"Simple Interest is {res}")
    except:
        Error.config(text="Please enter numbers only in the input fields !")
        pEntry.delete(0, tk.END)
        tEntry.delete(0, tk.END)
        rEntry.delete(0, tk.END)
        principal = 0
        time = 0
        rate = 0

window.title("basic CI and SI calculator")
principalClear = tk.Button(window, text="clear", command =lambda: pEntry.delete(0, tk.END))
rateClear = tk.Button(window, text="clear", command =lambda: rEntry.delete(0, tk.END))
timeClear = tk.Button(window, text="clear", command =lambda: tEntry.delete(0, tk.END))
welcome.grid()
creator.grid()
pStatement.grid()
pEntry.grid()
principalClear.grid()
rStatement.grid()
rEntry.grid()
rateClear.grid()
tStatement.grid()
tEntry.grid()
timeClear.grid()

def calculate():
    pass
window.mainloop()

