height=float(input("Enter height: "))
weight=float(input("Enter weight: "))
bmi=weight/(height**2)
if bmi<18.5:
    print("Underweight")
elif 18.5<=bmi<24.9:
    print("Normal")
elif 24.9<=bmi<29.9:
    print("Overweight")
elif 29.9<=bmi<34.9:
    print("Obesity class 1")
elif 34.9<=bmi<39.9:
    print("Obesity class 2")
elif bmi>=39.9:
    print("Obesity class 3")
else:
    print("severe obesity")
