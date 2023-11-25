Slip No-23

Que-1]
1. Write Python program to find the sum of first n natural numbers.
n=int(input("Enter Number:"))
s=0
for i in range(1,n):
    s=s+i
print("Sum=",s)


#2. Write Python code to prints all integers between 1 to 100 that are divisible by 3 and 7.
for i in range(1,100):
    if i%3==0 and i%7==0:
        print("Divisible=",i)

3. Write Python code to prints all integers between 1 to n, which are relatively prime to n.
n=int(input("Enter Number:"))
def prime(n):
    f=0
    for i in range(2,n):
       if n%i==0:
           f=1
           break
    if f==0:
       print(n,end=" ")
for i in range(2,n):
    prime(i) 



Que-2]
1. Write Python code to find determinant, transpose and inverse of matrix.
A =1 2 3
   2 5 7
   4 9 11
A=Matrix([[1,2,3],[2,5,7],[4,9,11]])
A.det()
A.T()
A.inv()

2. Write Python program to find the roots of the quadratic equation ax2 + bx + c = 0.


3. Using Python solve the following system of equations using LU – Factorization
method
 3x − 7y − 2z = −7
−3x + 5y + z = 5
 6x − 4y = 2







