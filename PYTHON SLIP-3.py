SLIP NO-3
Que-1]
1. Write python code to test whether given number is divisible by 2 or 3 or 5.
n=input("Enter Number:")
n=int(n)
if n%2==0 or n%3==0 or n%5==0:
    print("Number is Divisible by 2 or 3 or 5")
else:
    print("Number is not Divisible by 2 or 3 or 5")
    
2. Repeat the following string 11 times using the string operator ‘*’ on Python.
a. LATEX
a="LATEX"
print(a*11)

b. MATLAB
a="MATLAB"
print(a*11)

3.Use Python code to find sum of first thirty natural numbers
s=0
for i in range(1,31):
    s=s+i
print("Sum=",s)

Que-2]
1. Using Python construct the following matrices.
1. An identity matrix of order 10 × 10.
from sympy import*
eye(10,10)

2. Zero matrix of order 7 × 3.
zeros(7,3)

3. Ones matrix of order 5 × 4.
ones(5,4)

2. Using python, find the eigenvalues and corresponding eigenvectors of the matrix
3 −2
6 −4
from sympy import*
A=Matrix([[3,-2],[6,-4]])
A.eigenvals()
A.eigenvects()

3. Generate all the prime numbers between 1 to 100 using Python code.
import math
def phi(n):
    for x in range(1,100):
        if math.gcd(100,x)==1:
            print(x)

            
phi(100) 

