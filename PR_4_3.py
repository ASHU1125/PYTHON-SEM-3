weight_kg = float(input("enter weight in KG:"))
height_cm = float(input("enter height in CM:"))

height_m =height_cm / 100

bmi = weight_kg /(height_m**2)

if 19<= bmi <=25:
    print("The person is healthy.")
elif bmi < 19:
    print("The person is underweight.")
else:
    print("The person is overweight.")
    
    