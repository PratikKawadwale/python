Slip No-12

1. Using Python evaluate each of the following expression.
a. 23 modulus 2 + 9 - (3 +7) × 10 ÷ 2
a=23 % 2 + 9 - (3 +7) * 10 / 2
print(a)

b. 35 × 10 floor division 3 + 15 modulus 3
a= 35 * 10 // 3 + 15 % 3
print(a)

c. 35- 25 + 4 floor division 7
a=3**5 - 2**5 + 4 // 7
print(a)

#2. Use while command on Python to find odd positive integer between 25 to 50.


#3. For matrix A =1  0  5  4
                  2  1  6 -1
                  3  4  0  2
apply the following operations by using python.

A=Matrix([[1,0,5,4],[2,1,6,-1],[3,4,0,2]])

a. Delete 2nd row.
A.row_del(1)
A

b. Delete 1st column.
A.col_del(0)
A

c. Add column [9, 9] as 2nd column

Que-2]
1. Write Python find the eigenvalues and corresponding eigenvectors of the matrix
1 3 3
2 2 3
4 2 1


2. Write Python program to find the product of n natural numbers using while loop.


3. Generate all prime numbers between 1 to 200 using Python code.
def prime(n):
  f=0
  for i in range(2,n):
    if n%i==0:
      f=1
      break
  if f==0:
    print(n, end=" ")
for i in range(1,200):
  prime(i)









