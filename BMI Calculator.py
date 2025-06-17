def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if value < min_value or value > max_value:
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

print("Welcome to the BMI Calculator")

weight = get_valid_input("Enter your weight in kilograms (20 - 300): ", 20, 300)
height = get_valid_input("Enter your height in meters (1.0 - 2.5): ", 1.0, 2.5)

bmi = calculate_bmi(weight, height)
category = classify_bmi(bmi)

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Health Category: {category}")
