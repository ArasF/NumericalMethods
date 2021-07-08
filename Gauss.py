            ### GAUSSIAN ELIMINATION CODE ###

#Required modules numpy and sys 
import numpy as np
import sys
import time

#Openings with time(no need)
time.sleep(0.8)
print("Welcome to Gaussian Elimination Calculator ")
time.sleep(0.8)

# Taking number of unknowns
n= int(input('Enter number of unknowns: '))

""" adding 0 to all of the augmented matrix whicgh is (n*n+1)"""
a = np.zeros((n,n+1))
x = np.zeros(n)

# Taking augmented matrices coefficients with input
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

print("\nAugmented matrix is:")

for i in range(n):
    for j in range(n+1):
        print(f"{a[i][j]}", end="\t")
    print("\n")
    

# Gauss Elimination Code
for i in range(n):
    if a[i][i] == 0:
        sys.exit('Divide by zero is forbidden!')
        
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Back Substitution
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]

print('\n\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')

#Closing the code
time.sleep(0.8)
print("\nThe code is written by Aras Fırat\n")
time.sleep(2)
print("Good Bye!")