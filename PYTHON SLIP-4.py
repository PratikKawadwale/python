SLIP NO-4
1.Using python code sort the tuple in ascending and descending order 5,-3,0,1,6,-6,2.
a=(5,-3,0,1,6,-6,2)
print(a)
print("Ascending Order:",sorted(a))
print("Descending Order:",sorted(a,reverse=True))

2. Write python program which deals with concatenation and repetition of lists.
List1 = [15, 20, 25, 30, 35, 40]
List2 = [7, 14, 21, 28, 35, 42]

(a) Find List1 + List2
print(List1+List2)

(b) Find 9*List1
print(List1*9)

(c) Find 7*List2
print(List2*7)

3. Write Python code to find the square of odd numbers from 1 to 20 using while loop.

i=1
while i<=20:
    if i%2==1:
        print("Square of",i,"=",i*i)
    i=i+1

Que-2]
1. Using Python code construct the following matrices.
1. An identity matrix of order 10 × 10.
from sympy import*
eye(10)

2. Zero matrix of order 7 × 3.
zeros(7,3)

3. Ones matrix of order 5 × 4.
ones(4,4)

2. Find the data type of the following data by using Python code.
a. number
number=55
print(type(number))

b. 31.25
a=31.25
print(type(a))

c. 8 + 4j
a=8+4j
print(type(a))

d. Mathematics
a="Mathematics"
print(type(a))

e. 49
a=49
print(type(a))

3. Write Python program to find the determinant of matrices.
A =1 0 5   and B =2 5
   2 1 6         -1 4
   3 4 0
from sympy import*
A=Matrix([[1,0,5],[2,1,6],[3,4,0]])
A.det()

B=Matrix([[2,5],[-1,4]])
B.det()

