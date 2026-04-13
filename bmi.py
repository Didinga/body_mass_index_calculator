def calculate_bmi(height, weight):
    return round(weight / height ** 2, 1)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

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

if __name__ == "__main__":
    height = get_float("Enter your height in metres:\n")
    weight = get_float("Enter your weight in kilograms:\n")
    bmi = calculate_bmi(height, weight)
    print(f"Your BMI is: {bmi} ({get_category(bmi)})")
