# LAGRANGE INTERPOLATION

# Necesaary Libraries
import numpy as np

# Unknown Number
n = int(input('Enter number of data points: '))

#Making n*n array matrice's value to 0.
x = np.zeros((n))
y = np.zeros((n))



# Reading data points
print('Enter data points for x')
for i in range(n):
    x[i] = float(input( f"x[{str(i)}]="))
    

print('Enter data values for y')
for i in range(n):
    y[i] = float(input( f'y[{str(i)}]='))


    
# Reading interpolation point
inter_x = float(input('Enter interpolation point: '))

# Set interpolated value initially to zero
inter_y = 0

# Implementing Lagrange Interpolation
for i in range(n):
    
    temp = 1
    
    for j in range(n):
        if i != j:
            temp = (inter_x - x[j])/(x[i] - x[j])
    
    inter_y  = inter_y  + temp * y[i]    

# Displaying output
print('Interpolated value at %.6f is %.6f.' % (inter_x, inter_y))