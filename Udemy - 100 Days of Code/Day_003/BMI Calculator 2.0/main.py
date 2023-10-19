# Under 18.5 - Underweight
# Over 18.5 but below 25 - Normal weight
# Over 25 but below 30 - Slightly overweight
# Over 30 but below 35 - Obese
# Above 35 - Clinically obese


height = float(input("What is your height in meters?: "))
weight = int(input("What is your weight in kg?: "))

bmi = round((weight / height ** 2), 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you are normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi} and you are slightly obese.")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you are obese.")
else:
    print(f"Your BMI is {bmi} and you are clinically obese.")