
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

slope = (y2 - y1) / (x2 - x1)

print(f"The slope of the line between ({x1}, {y1}) and ({x2}, {y2}) is {slope}")
