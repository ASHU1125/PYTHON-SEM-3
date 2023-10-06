import math as m

height = float(input("Enter the height to reach (in meters): "))
angle_degrees = float(input("Enter the angle of the ladder (in degrees): "))

angle_radians = m.radians(angle_degrees)

ladder_length = height / m.sin(angle_radians)

print("The length of the ladder required is", ladder_length, "meters.")
   