Slip No-22

Que-1]
1. Write Python code to sort a tuples in ascending order (49, 17, 23, 54, 36, 72).
s=(49, 17, 23, 54, 36, 72)
print(sorted(s))

2. Find the values of the following expressions if x and y are true and z is false.
x=True
y=True
z=False
(a) (x or y) and z.
print((x or y) and z)

(b) (x and y) or not z.
print((x and y) or not z)

(c) (x and not y) or (x and z).
print((x and not y) or (x and z))

3. Write Python code to find the tuple ‘MATHEMATICS’ from range 3 to 9.
a="MATHEMATICS"
print(a[3:9])

Que-2]
1. Write Python program that prints whether the given number is positive, negative
or zero.
n=int(input("Enter Number:"))
if n==0:
    print("Number Is Zero....")
elif n%2==0:
    print("Number Is Even....")
else:
    print("Number Is Odd....")
    

2. Write Python program to find the sum of first n natural numbers.
s=0
n=int(input("Enter Number:"))
for i in range(1,n):
    s=s+i
print("Natural Numbers=",s)


#3. Using Python accept the matrix
A = 1 −3  2 −4
   −3  9 −1  5
    5 −2  6 −3
   −4 12  2  7
Find the Null space, Column space and rank of the matrix.
