Slip No-10
1. Using Python evaluate each of the following expression.
a. 50 modulus 5 + 11 - (13 +7) × 10 ÷ 5
a= 50%5 + 11 - (13 +7) * 10 / 5
print(a)

b. 60 × 20 floor division 3 + 15 modulus 3
a= 60 * 20 // 3 + 15 % 3
print(a)

c. 27- 23 + 8 floor division 4
a= 27- 23 + 8 // 4
print(a)

2. Using Python code
List1 = [5, 10, 15, 20, 25, 30] and List2 = [7, 14, 21, 28, 35, 42] Evaluate

List1 = [5, 10, 15, 20, 25, 30]
List2 = [7, 14, 21, 28, 35, 42]
(a) List1 + List2
print(List1+List2)

(b) 3*List1
print(List1*3)

(c) 5*List2
print(List2*5)

3. Write Python code to find area of triangle whose base is 10 and height is 15.
b=10
h=15
a=(b*h)/2
print("Area of Triangle:",a)

Que-2]
1. Using Python construct the following matrices.
1. An identity matrix of order 10 × 10.
from sympy import*
eye(10,10)

2. Zero matrix of order 7 × 3.
zeros(7,3)

3. Ones matrix of order 5 × 4.
ones(5,4)

#2. Write Python program to find the value of function f(x)=x2+x,(−5 ≤ x ≤ 5).

#3. Write Python program to find the determinant of matrix
A =1 0 5  and B= 2 5
   2 1 6        -1 4 
   3 4 0
A=Matrix([[1,0,5],[2,1,6],[3,4,0]])
A.det()

B=Matrix([[2,5],[-1,4]])
B.det()
















