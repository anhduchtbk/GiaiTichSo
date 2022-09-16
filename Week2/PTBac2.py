import math

def compute(a, b, c):
    delta = b ** 2 - 4 * a * c
    if(delta > 0):
        x1 = (float(-b) + math.sqrt(delta)) / (2 * float(a))
        x2 = (float(-b) - math.sqrt(delta)) / (2 * float(a))
        
        if(math.fabs(b - math.sqrt(delta)) <= 1e-6):
            x1 = (-4 * a * c) / (2 * a * (b + math.sqrt(delta)))
        elif(math.fabs(-b - math.sqrt(delta)) <= 1e-6):
            x2 = (-4 * a * c) / (2 * a * (b - math.sqrt(delta)))
        print("Nghiem cua pt x1 =", x1, " x2=", x2)
    elif(delta == 0):
        x = float(-b / (2 * a))
        print("Nghiem cua pt x=", x)
    else:
        print("VN")

compute(1, -(1e+9 + 1e-9), 1)
compute(1, -(1e+6 + 1e-6), 1e-6)