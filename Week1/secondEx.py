import numpy as np

x = float(input('x: '))

now = 2023
Pn = 0
for i in range(2024):
    Pn += now * np.power(x, now - 1)
    now -= 1

print(Pn)