def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than 0. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value. Try again.")

height = get_float("Enter your height in metres:\n")
weight = get_float("Enter your weight in kilograms:\n")

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