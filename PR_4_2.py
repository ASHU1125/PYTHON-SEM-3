hours_worked=float(input("Enter the number of hours worked:"))
hourly_rate=float(input("Enter the hourly rate:"))
if hours_worked <= 40:
    total_wages = hours_worked * hourly_rate
else:
    regular_wages = 40 * hourly_rate
    overtime_hours = hours_worked - 40 
    overtime_rate =  1.5 * hourly_rate
    total_wages = overtime_hours * overtime_rate
    
print("total wages = $",total_wages)