height = input("Enter your height in metres:\n")
weight = input("Enter your weight in kilograms:\n")

bmi = int(weight)/float(height)**2
bmi = int(bmi)
print("Your BMI is:"+str(bmi))
