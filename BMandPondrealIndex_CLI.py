#this is a CLI based BMI and Ponderal Index calculator 
def main():
    print("1 = BMI (default), 2 = Pnodreal Index")
    c1 = int(input("Choose if you want to use BMI index or Pondreal Index:"))
    if c1 == 1:
        BMIcalc()
    elif c1 == 2 :
        PIcalc()
    else:
        print("Invalid input! choosing BMI")
        BMIcalc()
def BMIcalc():
    print('''
          2 = Metric unit [kg, cm] (default)
          4 = Imperial units [lbs, in]
          ''')
    c2 =  int(input("Choose between metric and imperial units :"))
    if c2 == 2:
        BMIcalcSI()
    elif c2 == 4:
        BMIcalcImp()
    else:
        BMIcalcSI()
def PIcalc():
    print('''
          2 = Metric unit [kg, cm] (default)
          4 = Imperial units [lbs, in]
          ''')
    c3 =  int(input("Choose between metric and imperial units :"))
    if c3 == 2:
        BMIcalcSI()
    elif c3 == 4:
        BMIcalcImp()
    else:
        BMIcalcSI()
def BMIcalcSI():
    mass = int(input("Enter mass in 'kgs':"))
    h = int(input("Enter your height 'cm':"))
    hi = h/100
    BMI_SI = mass/hi**2
    print(f"Your BMI is {BMI_SI}")
#    yn = str(input("Would you like to know under which category your BMI mass is ? [y/n] (default = y):"))

def BMIcalcImp():
    mass = int(input("Enter your mass 'lbs':"))
    h = int(input("Enter your height 'in':"))
    BMI_Imp = 703*mass/h**2
    print(f"Your BMI is {BMI_Imp}")
def PIcalcSIImp():
    pass
def PIcalcSI():
    pass
main()