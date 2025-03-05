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
Calctype = tk.StringVar(value="SI")
si_radio = tk.Radiobutton(window, text="Simple Interest", variable=Calctype, value="SI")
ci_radio = tk.Radiobutton(window, text="Compound Interst", variable=Calctype, value= "CI")
si_radio.grid(row = 2, column=0,columnspan=1, padx=10, pady=10)
ci_radio.grid(row = 2, column=1, columnspan=2, padx=10, pady=10)
def preCalcFunc(i):
        if i=="SI":
            si_calculate(pEntry, rEntry, tEntry, Error, result)
        elif i=="CI":
            ci_calculate(pEntry, rEntry, tEntry, Error, result)
        else:
            Error.config(text="Please select a type of interest !")
calculateBtn = tk.Button(window, text="Calculate", command=lambda: preCalcFunc(Calctype.get()))
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
        Error.config(window, text="Please enter numbers only in the input fields !")
        pEntry.delete(0, tk.END)
        tEntry.delete(0, tk.END)
        rEntry.delete(0, tk.END)
        principal = 0
        time = 0
        rate = 0
resetBtn = tk.Button(window, text="Reset", command=lambda: Reset())
def Reset(pEntry, tEntry, rEntry, principal, time, rate):
        Error.config(window, text="")
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
welcome.grid(row= 0, column = 0,columnspan=2,padx=10,pady=10)
creator.grid(row = 1, column = 0,columnspan=2,padx=10,pady=10)
pStatement.grid(row  =3, column = 0,padx=10,pady=10)
pEntry.grid(row=3, column= 1,padx=10,pady=10)
principalClear.grid(row= 3, column= 2,padx=10,pady=10)
rStatement.grid(row =4, column =0,padx=10,pady=10 )
rEntry.grid(row=4, column= 1,padx=10,pady=10)
rateClear.grid(row= 4, column=2,padx=10,pady=10)
tStatement.grid(row=5,column=0,padx=10,pady=10)
tEntry.grid(row=5, column=1,padx=10,pady=10)
timeClear.grid(row=5, column=2,padx=10,pady=10)
calculateBtn.grid(row=6, column=3, padx=10, pady=10)
resetBtn.grid(row=6, column=2, padx=10, pady=10)
result.grid(row=6, column=0, padx=10, pady=10)
Error.grid(row=6, column=0, padx=10, pady=10)
def calculate():
    pass
window.mainloop()
