# def printMatrix(A, starting_index, rows, columns):
#     start_row, start_col = starting_index
    
  
#     for i in range(rows):
      
#         row_values = []
        
      
#         for j in range(columns):
#             current_row = start_row + i
#             current_col = start_col + j
            
          
#             if current_row < len(A) and current_col < len(A[0]):
#                 row_values.append(A[current_row][current_col])
 
#         if row_values:
#             print(' '.join(map(str, row_values)))


# A = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20]
# ]

# starting_index = (1, 2) 
# rows = 3
# columns = 4

# printMatrix(A, starting_index, rows, columns)


# def MatAdd(A, B):
   
#     rows = len(A)
#     if rows > 0 :
        
#         cols = len(A[0])
#     else :
#         cols = 0
    
   
#     result = [[0 for _ in range(cols)] for _ in range(rows)]
    
#     # Iterate through each element to perform addition
#     for i in range(rows):
#         for j in range(cols):
#             result[i][j] = A[i][j] + B[i][j]
    
#     return result

# A = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# B = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# result = MatAdd(A, B)

# for row in result:
#     print(row)


# def MatAddPartial(A, B, start, size):
#     start_row, start_col = start
    
   
#     result = [[0 for _ in range(size)] for _ in range(size)]
    
 
#     for i in range(size):
#         for j in range(size):
          
#             current_row = start_row + i
#             current_col = start_col + j
            
           
#             if current_row < len(A) and current_col < len(A[0]) and \
#                current_row < len(B) and current_col < len(B[0]):
#                 result[i][j] = A[current_row][current_col] + B[current_row][current_col]
#             else:
              
#                 result[i][j] = 0
    
#     return result

# A = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
   
# ]

# B = [
#     [5, 4, 3, 2, 1],
#     [10, 9, 8, 7, 6],
#     [15, 14, 13, 12, 11],
  
# ]

# start = (0, 1) 
# size = 2       
# result = MatAddPartial(A, B, start, size)

# # Print the result
# for row in result:
#     print(row)


# def MatMul(A, B):
   
#     rows_A = len(A)
#     cols_A = len(A[0])
#     rows_B = len(B)
#     cols_B = len(B[0])

  
#     if cols_A != rows_B:
#         raise ValueError("Number of cols in A must equal number of rows in B")

 
#     result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

 
#     for i in range(rows_A):
#         for j in range(cols_B):
#             for k in range(cols_A): 
#                 result[i][j] += A[i][k] * B[k][j]

#     return result

# A = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# B = [
#     [7, 8],
#     [9, 10],
#     [11, 12]
# ]

# result = MatMul(A, B)

# for row in result:
#     print(row)



# import numpy as np

# def MatMulRecursive(A, B):
#     # Base case: when the matrix is 1x1
#     if A.shape[0] == 1:
#         return A * B

#     # Partition matrices A and B into quadrants
#     mid = A.shape[0] // 2

#     A11, A12 = A[:mid, :mid], A[:mid, mid:]
#     A21, A22 = A[mid:, :mid], A[mid:, mid:]

#     B11, B12 = B[:mid, :mid], B[:mid, mid:]
#     B21, B22 = B[mid:, :mid], B[mid:, mid:]

#     # Recursively compute the quadrants of the result matrix
#     C11 = MatMulRecursive(A11, B11) + MatMulRecursive(A12, B21)
#     C12 = MatMulRecursive(A11, B12) + MatMulRecursive(A12, B22)
#     C21 = MatMulRecursive(A21, B11) + MatMulRecursive(A22, B21)
#     C22 = MatMulRecursive(A21, B12) + MatMulRecursive(A22, B22)

  
#     new_size = A.shape[0]
#     C = np.zeros((new_size, new_size))


#     C[:mid, :mid] = C11  
#     C[:mid, mid:] = C12  
#     C[mid:, :mid] = C21  
#     C[mid:, mid:] = C22  

#     return C

# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])

# C = MatMulRecursive(A, B)
# print(C)

import numpy as np

def add_matrices(A, B):
    return A + B

def subtract_matrices(A, B):
    return A - B

def MatMulStrassen(A, B):
    # Base case: 
    if A.shape[0] == 1:
        return A * B

    n = A.shape[0]
    if n % 2 != 0: 
        A = np.pad(A, ((0, 1), (0, 1)), mode='constant')
        B = np.pad(B, ((0, 1), (0, 1)), mode='constant')

    mid = n // 2

    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

   
    M1 = MatMulStrassen(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = MatMulStrassen(add_matrices(A21, A22), B11)
    M3 = MatMulStrassen(A11, subtract_matrices(B12, B22))
    M4 = MatMulStrassen(A22, subtract_matrices(B21, B11))
    M5 = MatMulStrassen(add_matrices(A11, A12), B22)
    M6 = MatMulStrassen(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = MatMulStrassen(subtract_matrices(A12, A22), add_matrices(B21, B22))

    # Combine the results into the final matrix
    C11 = add_matrices(subtract_matrices(add_matrices(M1, M4), M5), M7)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = add_matrices(subtract_matrices(add_matrices(M1, M3), M2), M6)

    new_size = A.shape[0]
    C = np.zeros((new_size, new_size))
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22

    return C


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = MatMulStrassen(A, B)
print(C)


