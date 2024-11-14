def bmi_calc():
    mass=float(input("Enter your weight in kilograms:"))
    height=float(input("Enter your heigh in meters:"))
    bmi=mass/(height*height)
    if bmi<16:
        print("Your are underweight (Severe thinness),focus on increasing weight")
    elif bmi>=16 and bmi<=16.9:
        print("our are underweight (Moderate thinness)")  
    elif bmi>=17 and bmi<=18.4:
        print("Underweight (Mild thinness)")
    elif bmi>=18.5 and bmi<=24.9:
        print("Normal range")
    elif bmi>=25 and bmi<=29.9:
        print("Overweight (Pre obese)")
    elif bmi>=30 and bmi<=34.9:
        print("Obese(class I)")
    elif bmi>=35 and bmi<=39.9:
        print("Obese(class II)")
    elif bmi>=40:
        print("Obese(class III)")
    r=round(bmi,2)
    print(r)
bmi_calc()