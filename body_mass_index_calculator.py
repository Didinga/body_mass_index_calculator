height = float(input("Enter your height in metres:\n"))
weight = float(input("Enter your weight in kilograms:\n"))

bmi = round(weight / height ** 2, 1)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is: {bmi} ({category})")