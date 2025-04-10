h=float(input("Enter your height in meters:"))
w=float(input("Enter your weight in kg:"))

BMI=w/(h**2)
print("BMI :",BMI)

if BMI <=18.5:
    print("underweight")
elif BMI >18.5 and BMI<25:
    print("Healthy")
elif BMI >25 and BMI<28:
    print("Over weight")
else:
    print("Obese")