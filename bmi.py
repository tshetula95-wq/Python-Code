weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Your BMI is:", bmi, "which is considered Underweight.")
elif 18.5 <= bmi < 25:
    print("Your BMI is:", bmi, "which is considered Normal.")
elif 25 <= bmi < 30:
    print("Your BMI is:", bmi, "which is considered Overweight.")
else:
    print("Your BMI is:", bmi, "which is considered Obese.")

