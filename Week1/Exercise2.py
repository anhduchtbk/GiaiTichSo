from math import factorial
# a
def macLaurin():
    e = 1
    for i in range(1, 1000 + 1):
        e += 1 / factorial(i)
    return e
print(macLaurin())

# b
