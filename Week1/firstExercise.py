# Viết hàm imput xâu
#   A = [a0 a1 ... an] và x chuyển dạng 'string' sang 'float'
#   Tính giá trị đa thức Pn(x) = p^2 Horner 
#   Pn(x) = an.x^n + an-1 . x^(n-1) + ... + a1.x + a0
import numpy as np

# In1 = input('your input 1: ')
# In2 = input('your input 2: ')

# A = In1.split(' ')
# x = float(In2)
# Pn = 0
# index = 0

# for i in range(len(A)):
#     Pn += float(A[index]) * np.power(x, i);
#     index += 1

# print(Pn)


# fist way
def convertStr():
    In = input('your input: ')
    A = In.split(' ')
    return A


def unHorner(A, x):
    Pn = 0
    # index = 0
    for i in range(len(A)):
        Pn += float(A[i]) * np.power(float(x), i);
        # index += 1
    print(A)
    print(Pn)



# other way
def horner(A, x):
    # x = A.pop()
    n = len(A)
    Pn = float(A[n - 1])
    while(n > 1):
        Pn = Pn * float(x) + float(A[n - 2])
        n -= 1
    print(A)
    print(Pn)

A = convertStr()
x = A.pop()
print('not use horner: ')
unHorner(A, x)
print('nuse horner:')
horner(A, x)