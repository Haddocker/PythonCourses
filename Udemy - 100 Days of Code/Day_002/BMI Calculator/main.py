height = input("What is your height in meters?: ")
weight = input("What is your weight in kg?: ")

# BMI Calculation
# BMI = weight(kg) / height^2 (m^2)



### My code:
# bmi = float(weight) / float(height) ** 2
# bmi = int(bmi)
# pri-nt(f"Your BMI is {bmi}")



### Udemy code:
weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
# bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)