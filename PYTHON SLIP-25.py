Slip No-25

Que-1]
1. Write Python program to print the integers between 1 and 1000 which are multiples
of 7.


2. Write Python program to prints whether the given number is divisible by 3 or 5 or 7.
n=int(input("Enter Number:"))
if n%3==0 or n%5==0 or n%7==0:
    print("Number is Divisible by 3 or 5 or 7..")
else:
    print("Number is not Divisible by 3 or 5 or 7..")


3. Write Python code to find A + B and B ∗ A for the given Matrices.
A = 4  2  4  & B=5  2  3
    4 −1  1      3 -7  5
    2  4  2      3  1 -1 
A=Matrix([[4,3,4],[4,-1,1],[2,4,2]])
B=Matrix([[5,2,3],[3,-7,5],[3,1,-1]])
print(A+B)
print(B*A)


Q.2. Attempt any two of the following. [10]
1. Write Python program to find the area and circumference of a circle with radius r.
r=float(input("Enter Radius:"))
c=2*3.14*r
print("Circumference Of Circle:",c)

2. Use Python code to solve the following system of equations by gauss elimination
method
x + y + 2z = 7
−x − 2y + 3z = 6
3x − 7y + 6z = 1


3. Write Python code to find eigen values, eigen vectors of the matrix and determine
whether the matrix is diagonalizable.
A = 1 −1  1
   −1  1 −1
    1 −1  1






