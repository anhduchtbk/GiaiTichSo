from numpy import dot
import scipy.linalg as la
import numpy as np
A = [[2, 4, 3], [3, 1, -2], [4, 11, 7]]
b = [[3], [3], [4]]
L = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# AA = np.array(A)
# bb = np.array(b)
# P, LL, U = la.lu(AA)
# print("solve:", la.solve(AA, bb))
# print("L:",LL)
# print("U:", U)
def gauss(A, b):
    c = 0 #cot ma tran
    while(c < len(A) - 1):
        for i in range(c + 1, len(A)):
            h = float(A[i][c] / A[c][c])
            b[i][0] = b[i][0] - h * b[c][0]
            for k in range(c, len(A)):
                A[i][k] = float(A[i][k] - h * A[c][k])
                L[i][c] = h 
        c += 1 
    print("L:", L)
    print("U:",A)
    print("b:",b)
'''
    x1 x2 x3 | b1
    0  x2 x3 | b2
    0  0  x3 | b3
'''
def find_x():
    x3 = b[2][0] / A[2][2]
    x2 = (b[1][0] - x3 * A[1][2]) / A[1][1]
    x1 = (b[0][0] - x2 * A[0][1] - x3 * A[0][2]) / A[0][0]
    print("x:[",x1, x2, x3,"]")

gauss(A, b)
find_x()



        