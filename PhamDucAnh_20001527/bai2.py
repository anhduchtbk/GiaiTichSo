# import numpy as np
# import scipy.linalg as la



from numpy import dot
import scipy.linalg as la
import numpy as np
from math import fabs as ab

A = [[89, 59, 77], [59, 107, 59], [77, 59, 89]]
b = [[18], [2], [85]]
L = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
P = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def swap_L(B): # doi cho hang ma tran L moi khi pivot
    temp = B[1][0]
    B[1][0] = B[2][0]
    B[2][0] = temp 

def sort(B, b,i): # i la co ma tran dang duoc xet
    for j in range(len(B) - 1): # hang cua ma tran
        for k in range(j + 1, len(B)): # hang ma tran
            if(j >= i and ab(B[j][i]) < ab(B[k][i])):
                swap(B, j, k)
                swap_L(L)
                swap(b, j, k)
                swap(P, j, k)

def swap(B, i, c):
    temp = B[i]
    B[i] = B[c]
    B[c] = temp

def gauss(A, b):
    c = 0 #cot ma tran
    while(c < len(A) - 1):
        sort(A, b, c)
        for i in range(c + 1, len(A)):
            h = float(A[i][c] / A[c][c])
            b[i][0] = b[i][0] - h * b[c][0]
            for k in range(c, len(A)):
                A[i][k] = float(A[i][k] - h * A[c][k])
                L[i][c] = h  
        c += 1 
    
    print("L:", L)
    print("U:", A)
    print("b:", b)

'''
    x1 x2 x3 | b1
    0  x2 x3 | b2
    0  0  x3 | b3
'''

def find_x():
    x3 = b[2][0] / A[2][2]
    x2 = (b[1][0] - x3) / A[1][1]
    x1 = (b[0][0] - x2 - x3) / A[0][0]
    print("x:[",x1, x2, x3,"]")


gauss(A, b)
find_x()

A = np.array([[89, 59, 77], [59, 107, 59], [77, 59, 89]])
b = np.array([[18], [2], [85]])

L = la.cholesky(A)
print("L:", L)

Q, R = np.linalg.qr(A)
print(Q)
print(R)

U1, S, V = np.linalg.svd(A)
print("U1", U1)
print("S", S)
print("V", V)