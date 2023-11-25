SLIP NO-1

Q.1. any two [10]
1. Use Python code to evaluate each of the following expression.

a. 20 modulus 2 + 7 - (3 +7) × 20 ÷ 2
ans=20%2+7-(3+7)*20/2
print(ans)

b. 30 × 10 floor division 3 + 10 modulus 3
ans=30*10//3+10%3
print(ans)

c. 2^5- 2^4 + 4 floor division 4
ans=2**5-2**4+4//4
print(ans)

2. Write Python code to repeat the following string 9 times using the string operator ‘*’.
a. Python
s="python"
print(s*9)

b. Mathematics
s="mathematics"
print(s*9)

3. Write Python program to generate the square of numbers from 1 to 10.
for i in range(1,11):
    print("square of",i,"=",i*i)

Q.2. any two  [10]
1. Using Python code construct the following matrices.
1. An identity matrix of order 10 × 10.
from sympy import*
eye(10)

2. Zero matrix of order 7 × 3.
from sympy import*
zeros(7,3)

3. Ones matrix of order 5 × 4.
from sympy import*
ones(4,4)

2. Write Python program to find the 10 term of the sequence of function f(x)=x**2+x.
def f(x):
    return x**2+x
for x in range(1,11):
    print(f(x),end=" ")

3. Generate all the prime numbers between 1 to 100 using Python code.
import math
def phi(n):
    for x in range(1,100):
        if math.gcd(100,x)==1:
            print(x)

            
phi(100) 

Q.3. a. Attempt any one of the following. [7]
1. Write Python program to estimate the value of the integral /π 0 sin(x)dx using Simpson’s (1/3)rd rule (n=6).	
def simpson13(f,a,b,n):
    h=float(b-a)/n
    result=f(a)+f(b)
    for i in range(1,n):
        k=a+i*h
        if i%2==0:
           result=result+2*f(k)
        else:
            result=result+4*f(k)
    result=result*h/3
    return result

def f(x):
    return sin(x)

from math import*
simpson13(f,0,pi,6)

2. Write Python program to evaluate interpolate value f(3) of the given data by Lagranges method.
x       0   1   2   5
Y=f(x)  5   13  22  129

b. Attempt any one of the following. [8]

1.Write Python program to obtained the approximate real root of x3−4x−9=0 by using Regula-falsi method.

2.Write Python program to estimate the value of the integral /10 2  1/(1+x)dx using Trapezoidal rule (n=8).
