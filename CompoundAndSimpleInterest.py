def simIntCalc(pri, rate, time):
    val1 = pri*rate*time
    return val1/100
def total_amount(p, i):
    return p+i
def compoundInterest(pri, rate, time):
    #CI = P*(1+R/100)**T-P
    return pri*(1+rate/100)**time-pri 
pri = float(input("Principal amount:"))
rate = float(input("rate of Interest (%):"))
time = float(input("Time (in years):"))
print('''Please choose one:
        1 = Simple Interest (S.I.)[default]
        2 = Compund Interest (C.I.)
      ''')
c1 = int(input("Please enter your selection [1/2]: "))
v1 = simIntCalc(pri, rate, time)
v2 = compoundInterest(pri, rate, time)
if c1 == 1:
    print(f"Your Simple Interest is {v1:.2f}")
    c2 = input("Do you want to see the total amount ? [y/n]")
    if c2.lower() == "y":
        print(f"Your total for Simple interest is {pri + v1}")
    elif c2.lower() == "n":
        print("Thank you for using the calculator !")
    else:
        print("Inavalid input ! taking default input as \"y\"")
        print(f"Your total for Simple interest is {pri + v1}")
elif c1 == 2:
    print(f"Your Compound Interest is {v2:.2f}")
    c2 = input("Do you want to see the total amount ? [y/n]")
    if c2.lower() == "y":
        print(f"Your total for Compound interest is {pri + v2}")
    elif c2.lower() == "n":
        print("Thank you for using the calculator !")
    else:
        print("Inavalid input ! taking default input as \"y\"")
        print(f"Your total for Compound interest is {pri + v2}")
else :
    print("Invalid selection choosing [1] !")
    print(f"Your Simple Interest is {v1:.2f}")
#print(f"your simple interest is {simIntCalc(pri, rate, time)}")
#print(f"your total amount is {total_amount(pri, simIntCalc(pri, rate, time))}")
