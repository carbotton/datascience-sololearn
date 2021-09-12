################################################################################
#In a matrix, or 2-d array X, the averages (or means) of the elements of rows is called row means. 
 
#Task 
#Given a 2D array, return the rowmeans. 
 
#Input Format 
#First line: two integers separated by spaces, the first indicates the rows of matrix X (n) and the second indicates the columns of X (p) 
#Next n lines: values of the row in X 
 
#Output Format 
#An numpy 1d array of values rounded to the second decimal. 
 
#2 2 
#1.5 1 
#2 2.9 
 
#Sample Output 
#[1.25 2.45]

################################################################################


import numpy as np

n, p = [int(x) for x in input().split()]

# Initialize matrix
matrix = []

#Entry row elements separated by space
for i in range(n):
  matrix.append(input().split())
  
print(np.array(matrix).astype(np.float16).mean(axis=1).round(2))

#For entries rowwise
# For user input
#for i in range(n):		 # A for loop for row entries
#	a = []
#	for j in range(p):	 # A for loop for column entries
#		a.append(float(input()))
#	matrix.append(a)


# For printing the matrix
#for i in range(n):
#	for j in range(p):
#		print(matrix[i][j], end = " ")
#	print()
