Slip No-6

Que-1]
1. Using Python evaluate each of the following expression.
a. 23 modulus 2 + 9 - (3 +7) × 10 ÷ 2
ans=23%2+9-(3+7)*10/2
print(ans)

b. 35 × 10 floor division 3 + 15 modulus 3
ans=35*10//3+15%3
print(ans)

c. 3^5 − 2^5 + 4 floor division 7
ans=3**5-2**5+4//7
print(ans)

2. Write Python code to list name and roll number of 5 students in B.Sc.
(Computer science)
a=[{"NAME":"OM","ROLLNO":101},
   {"NAME":"SAI","ROLLNO":102},
   {"NAME":"RAM","ROLLNO":103},
   {"NAME":"SHAM","ROLLNO":104},
   {"NAME":"AMAN","ROLLNO":105}]
print(a)

3. Write Python code to find maximum and minimum element in the given list.
[7, 8, 71, 32, 49, −5, 7, 7, 0, 1, 6]
s=[7, 8, 71, 32, 49, -5, 7, 7, 0, 1, 6]
s1={}
s1=set(s)
s=list(s1)
s.sort()
print(s)
print("Minimum Element:",s[0])
print("Maximum Element:",s[-1])


Que-2]
1. Using Python code construct identity matrix of order 10 and hence
find determinant,trace and transpose of it.
from sympy import*
A=eye(10)
A.det()
A.trace()
A.T

2. Write Python code to find the value of function f(x,y)=x2−2xy+4 at
the points(2,0)(1,-1).
def f(x,y):
    return f(x,y)=x**2−2*x*y+4
print((2,0),end=" ")
print((1,-1),end=" ")


3. Find number between 1 to 200 which are divisible by 7 using Python code.
for i in range(1,200):
    if i%7==0:
        print(i,end=" ")
       




    














