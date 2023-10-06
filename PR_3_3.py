P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest (in percentage): "))
T = float(input("Enter the time period (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

Simple_Interest = (P * R * T) / 100
print("Simple Interest =", Simple_Interest)

def compound_interest(P, R, T, n):
    CI = P * (1 + (R / 100) / n) ** (n * T)
    return CI

Compound_Interest = compound_interest(P, R, T, n)
print("Compound Interest =", Compound_Interest)
