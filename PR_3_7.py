import math as m
a = float(input("enter the value of a :"))
b = float(input("enter the value of b :"))
c = float(input("enter the value of c :"))


discriminant = b**2-4*a*c

if discriminant >= 0:
    
 realroot1 = (-b + m.sqrt(discriminant)) /(2*a)
 realroot2 = (-b - m.sqrt(discriminant)) / (2*a) 

 print("discriminant=", discriminant)
 print("realroots =",realroot1,"or",realroot2)
else : 
 print ( "no real roots")
  