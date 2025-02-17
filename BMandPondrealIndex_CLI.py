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
def PIcalcImp():
    mass = int(input("Child's mass 'lbs':"))
    h = int(input("Child's height 'in':"))
    h1 = h*2.54
    m1= mass*0.45
    PI = m1/h1**3
    print(f"your pondreal index value is {PI}")
def PIcalcImp_adult():
    print("The imperial section is still under progress please cross-check from other sources if possible")
    mass = int(input("Enter your mass 'lbs':"))
    h = int(input("Enter height 'in':"))
    h1 = h*2.54
    m1 = mass*0.45
    PI = m1/h1**3
    print(f"your pondreal index value is {PI}")
def PIcalcSI():
    mass = int(input("Enter child's mass 'kgs':"))
    h = int(input("Enter child's height 'cms':"))
    h1 = h/100
    m1 = mass*100
    PI = m1/h1**3
    print(f"child/infant's pondreal index value is {PI}")
def PIcalcSI_adult():
    mass = int(input("Enter your mass 'kgs':"))
    h = int(input("Enter height 'cms':"))
    h1 = h/100
    PI = mass/h1**3
    print(f"your pondreal index value is {PI}")
def PIcalc_pre():
    print(
        '''
        => Pondreal Index is only a proxy measure for adiposity therefore 
        if you have a lot of muscle mass and are categorized as 'overweight'
        dont worry ;)
        Caclulation needs to be done for an/a infant/child or for adult?
        3 = infant/child
        5 =  adult
        ''')
    c3 = int(input("Enter your selectio, adult or child/infant [3(default)/5]: "))
    if c3 == 3:
        PIcalc()
    elif c3 == 5:
        PIcalc_adult()
    else:
        PIcalc()
def PIcalc_adult():
    print('''
          2 = Metric unit [kg, cm] (default)
          4 = Imperial units [lbs, in]
          ''')
    c3 =  int(input("Choose between metric and imperial units :"))
    if c3 == 2:
        PIcalcSI_adult()
    elif c3 == 4:
        PIcalcImp_adult()
    else:
        PIcalcSI_adult()
def PIcalc():
    print('''
          2 = Metric unit [kg, cm] (default)
          4 = Imperial units [lbs, in]
          ''')
    c3 =  int(input("Choose between metric and imperial units :"))
    if c3 == 2:
        PIcalcSI()
    elif c3 == 4:
        PIcalcImp()
    else:
        PIcalcSI()

main()
