
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

max_num = num1 if (num1 > num2 and num1 > num3) else (num2 if (num2 > num3) else num3)

print("The maximum number is:", max_num)
