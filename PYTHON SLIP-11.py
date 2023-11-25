Slip NO-11
1. Evaluate following expression on Python.
(a) M =[1,2,3,4,5,6,7], Find length M.
M =[1,2,3,4,5,6,7]
print(len(M))

(b) L=“XY”+“pqr”, Find L.
L="XY"+"pqr"
print(L)

(c) s=‘Make In India’, Find (s[:5]) & (s[:9]).
s="Make In India"
print(s[:5])
print(s[:9])

2. Use Python to evaluate expression of the following matrix.
A =1 1 1
   0 1 1
   0 0 1
from sympy import*
A=Matrix([[1,1,1],[0,1,1],[0,0,1]])
(a) Eigen Value of A.
A.eigenvals()

(b) determinant of A.
A.det()

(c) inverse of A.
A.inv()

3. Write Python code to reverse the string S=[3,4,5,6,7,8,9,10,11,12,13].
S=[3,4,5,6,7,8,9,10,11,12,13]
print(S[::-1]
      
Que-2]
1. Using Python code to list Name of 5 teacher in your college with their subject.
a=[{"Name":"Mhaske","Subject":"Electronics"},
  {"Name":"Shinde","Subject":"DS"},
  {"Name":"Unde","Subject":"C Lang"},
  {"Name":"Bhakre","Subject":"math"},
  {"Name":"Lande","Subject":"Electronics-1"}]
print(a)

2. Use linsolve command in python to solve the following system of linear equations.
x − 2y + 3z = 7
2x + y + z = 4
−3x + 2y − 2z = −10

A=Matrix([[1,-2,3],[2,1,1],[-3,2,-2]])
B=Matrix([[7,4,-10]])
linsolve((A,B))


3. Generate all the prime numbers between 51 to 100 using Python program.
def prime(n):
  f=0
  for i in range(2,n):
    if n%i==0:
      f=1
      break
  if f==0:
    print(n, end=" ")
for i in range(51, 100):
  prime(i)

