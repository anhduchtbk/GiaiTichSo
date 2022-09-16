import math

def atan(x):
    x = float(x)
    actan = x - float((1 / 3) * (x ** 3)) + float((1 / 5) * (x**5))
    return actan
# pi
result1 = 4 * (atan(1 / 2) + atan(1 / 3))
print("%.6f"%result1)
# pi
result1 = 16 * (atan(1/ 5)) - atan(1 / 239)
print("%.6f"%result1)
