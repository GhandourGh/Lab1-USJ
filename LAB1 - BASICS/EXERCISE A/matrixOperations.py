import numpy as np
import matplotlib.pyplot as plt
from numpy.ma.core import identity


########
# 1
########


def print_matrix(m, label):
    '''
   m is a 2D list(list of lists
   label is a string, name of the matrix(ex A)\
   '''
    print(label, "=")
    for row in m:  #go over each row
        print(row)


########
# 2 #
#########

def identity_matrix(n):  #Retun n*n matrix with 1 on the diagonal
    #Create an empy matrix
    #loop from 0 to n-1(rows)
    #inside each row, loop from 0 to n-1 (columns)
    #if row == column then put 1
    #else put 0
    #return matrix
    matrix = []

    for row in range(n):
        c_row = []
        matrix.append(c_row)
        for col in range(n):
            if row == col:
                c_row.append(1)
            else:
                c_row.append(0)
    return matrix


"""print(identity_matrix(3))
print_matrix(identity_matrix(3), "Identity")"""


###########
#### 3 ####
###########

def transpose(m):
    row = len(m)
    col = len(m[0])
    matrix = []
    for i in range(col):
        new_row = []
        for j in range(row):
            new_row.append(m[j][i])
        matrix.append(new_row)
    return matrix


M = [[1, 2, 2], [2, 1, -2], [2, -2, 1]]
print_matrix(M, "Matrix = ")
print_matrix(transpose(M), "Transpose = ")

###########
#### 4 ####
###########

def mult_row_scalar(M, row, scalar):
    cols = len(M[row])
    for j in range(cols):
        M[row][j] *= scalar
    return M

mult_row_scalar(M, 1, 10)
mult_row_scalar(M, 2, 10)
print_matrix(M, "Matrix = ")

###########
#### 5 ####
###########


