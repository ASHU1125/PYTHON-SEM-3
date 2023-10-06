positive, negative, zero, odd, even, total = 0, 0, 0, 0, 0, 0

n = int(input("Enter the number of values (n): "))

for i in range(n):
    num = float(input("Enter a number: "))
    
    total += num
    positive += num > 0
    negative += num < 0
    zero += num == 0
    even += num % 2 == 0
    odd += num % 2 != 0
    
    

average = total/ n if n > 0 else 0

print("Number of positive numbers:", positive)
print("Number of negative numbers:", negative)
print("Number of zeros:", zero)
print("Number of odd numbers:", odd)
print("Number of even numbers:", even)
print("Average of all numbers:", average)
