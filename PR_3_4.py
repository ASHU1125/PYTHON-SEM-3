
quarter_value = 0.25
dime_value = 0.10
nickel_value = 0.05
penny_value = 0.01

quarters = float(input("Enter the number of quarters: "))
dimes = float(input("Enter the number of dimes: "))
nickels = float(input("Enter the number of nickels: "))
pennies = float(input("Enter the number of pennies: "))

total_value = (quarters * quarter_value) + (dimes * dime_value) + (nickels * nickel_value) + (pennies * penny_value)

print(f'Total value of change: ${total_value:.2f}')
