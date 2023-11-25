Slip No-15

Que-1]
1. Using for loop on Python, find range from 1 to 11 integers.
for i in range(1,12):
    print(i)

2. Use Python code to find,
(a) sin75
from math import sin
a=sin(75)
print(a)

(b) pi/2
from math import pi
a=pi/2
print(a)

(c) e
from math import e
a=e
print(a)

(d) cos56
from math import cos
a=cos(56)
print(a)

3. Write Python program to find diameter,area,circumference of the circle with radius is 5.
r=5
d=2*r
a=3.14*r*r
c=2*3.14*r
print("Diameter of Circle:",d)
print("Area of Circle:",a)
print("Circumference of Circle:",c)

Que-2]
#1.Using Python code construct any three matrices A,B and C to show that
(A+B)+C=A+(B+C).

#2. Using python find the eigenvalues and corresponding eigenvectors of the matrix
3 −2
6 −4 
A=Matrix([[3,-2],[6,-4]])
A.eigenvals()
A.eigenvects()

3. Generate all prime numbers between 1000 to 2000 using Python program.
def prime(n):
  f=0
  for i in range(2,n):
    if n%i==0:
      f=1
      break
  if f==0:
    print(n, end=" ")
for i in range(1000,2000):
  prime(i)

     





