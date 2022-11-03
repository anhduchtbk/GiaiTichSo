# import pprint
# import scipy
# import scipy.linalg 

# A = scipy.array([ [3, 17, 10], [2, 4, -2], [6, 18, -12]])
# P, L, U = scipy.linalg.lu(A)

# print ("A:")
# pprint.pprint(A)

# print ("P:")
# pprint.pprint(P)

# print ("L:")
# pprint.pprint(L)

# print ("U:")
# pprint.pprint(U)

from numpy import dot
import scipy.linalg as la
import numpy as np
from math import fabs as ab

A = [[4, 5, -2], [2, -5, 2], [6, 2, 4]]
b = [[30], [4], [12]]
L = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
P = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

AA = np.array(A)
bb = np.array(b)
PP, LL, U = la.lu(AA)
print("P:", PP)
print("L:",LL)
print("U:", U)

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


        