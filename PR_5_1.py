n = int(input("Enter the number of values (n): "))
total = 0

for i in range(n):
    total += float(input(f"Enter number {i + 1}: "))

average = total / n
print(f"The average of {n} numbers is: {average}")