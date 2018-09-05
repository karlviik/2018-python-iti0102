"""Greets user based on input, calculates BMI and outputs body classification."""
name = input("What is your name?:")
if name == "":
    print("Name was not inserted!")
    exit()
school = input("Where do you study?:")
if school == "":
    print("School was not inserted!")
    exit()
print(f"{name}, welcome to {school}")
mass = float(input("Please enter your weight in kilograms:"))
height = float(input("Please enter your height in meters:"))
bmi = mass / height ** 2
body_type = ""
if bmi < 18.5:
    body_type = "alakaaluline"
elif bmi > 25.0:
    body_type = "ülekaaluline"
else:
    body_type = "normaalkaal"
print(f"{bmi}, {body_type}")
