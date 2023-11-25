Slip No-5

Que-1]
1. Using sympy module of python find the following for the matrices
A =−1  1  0   and B =9  0  3
    8  5  2          1  4  1 
    2 −6  2          1  0 -1    
from sympy import*
A=Matrix([[-1,1,0],[8,5,2],[2,-6,2]])
B=Matrix([[9,0,3],[1,4,1],[1,0,-1]])
(a) 2A + B.
2*A+B

(b) 3A – 5B.
3*A-5*B

(c) A−1.
A.inv()

(d) B3.
B*3

(e) AT + BT.
A.T + B.T

2. Evaluate following expression on Python.
(a) M =[1,2,3,4], Find length M.
M=[1,2,3,4]
len(M)

(b) L=“XYZ”+“pqr”, Find L.
L="XYZ"+"pqr"
print(L)

(c) s=‘Make In India’, Find (s[:7]) & (s[:9]).
s="Make In India"
s[:7]
s[:9]

3. Use Python code to generate the square root of numbers from 21 to 49.
from math import*
for i in range(21,50):
    print("Square Root of",i,"=",sqrt(i))

Que-2]
1. Using Python construct the following matrices.
1. An identity matrix of order 10 × 10.
from sympy import*
eye(10,10)

2. Zero matrix of order 7 × 3.
zeros(7,3)

3. Ones matrix of order 5 × 4.
ones(5,4)

2. Using linsolve command in python, solve the following system of linear equations.
x − 2y + 3z = 7
2x + y + z = 4
−3x + 2y − 2z = −10
from sympy import*
A=Matrix([[1,-2,3],[2,1,1],[-3,2,-2]])
B=Matrix([[7,4,-10]])
linsolve((A,B))

3. Generate all relatively prime numbers to 111 which are less than 150 using Python
code.
from math import*
for i in range(1,150):
    if gcd(111,i)==1:
        print(i,end=" ")
        







