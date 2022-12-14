from scipy import linalg
import numpy as np

# cholesky
matrix = np.array([[4, -2, 4], [-2, 5, -4], [4, -4, 6]])
print(linalg.cholesky(matrix))
print(np.linalg.cholesky(matrix))
# tim ma tran nghich dao A^-1
# bang PLU

# cho ma trận A gọi ma trận A1 là ghép của ma trận A và ma trận đơn vị A1:= [A | In]
# giải bằng phương pháp PLU: P, L, U1 = [U | Z]
# tiếp tục giải U.x[:,i] = Z[:,i]

A =  np.array([[1, 2, 4], [1, 3, 9], [1, 4, 16]])
In = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

A1 = np.hstack((A, In))
print(A1)
P, L, U1 = linalg.lu(A1)
# print(U1)
# U1 = [U | Z]
U = U1[:, :3]
# print(U)
def find_x(Z):
    x3 = Z[2] / U[2,2]
    x2 = (Z[1] - U[1,2] * x3) / U[1, 1]
    x1 = (Z[0] - U[0,2] * x3 - U[0, 1] * x2) / U[0, 0]
    arr = np.array([[x1], [x2], [x3]])
    return arr

x = np.array([[], [], []])

for i in range(len(U[0])):
    x = np.hstack((x,find_x(U1[:, 3 + i])))
print(x)

# print(linalg.inv(A))


# from time import time

# def Newton(f, df, x0, tol):
#     x_old = x0
#     while(abs(f(x_old)) > tol and df(x_old) != 0):
#         x_new = x_old - f(x_old) / df(x_old)
#         x_old = x_new
#     return x_old
# f = lambda x: x - x**(1/3) - 2
# df = lambda x: 1 - 1/3 * x**(-2/3)
# x0 = 2.5
# tol = 1e-6
# tic = time()
# x = Newton(f, df, x0, tol)
# toc = time()
# print ( 'No su dung phuong phap Newton la:',x)
# print('Processing tiem is =', toc - tic)