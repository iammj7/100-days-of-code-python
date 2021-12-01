height = float(input("What is your height in m: "))
weight = float(input("What is your weight in kg: "))

bmi = round(weight / height **2)

if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are under weight')
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi}, your Over weight")
elif bmi > 30 and bmi < 35:
    print(f'Your BMI is {bmi}, You are Obese.')
else:
    print(f'Your BMI is {bmi}, Your Clinically obese')
