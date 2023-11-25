Slip No-19

Que-1]
#1. Write python code to display multiplication tables of numbers 2 to 10.

for i in range(2,10):
    print("Multiplication Tables",i,"=",i*2)

2. Write Python code to check if a number is Zero, Odd or Even.
n=int(input("Enter Number:"))
if n==0:
    print("Number Is Zero....")
elif n%2==0:
    print("Number Is Even....")
else:
    print("Number Is Odd....")
    

3. Write Python code to list name and birth date of 5 students in your class.
a=[{"NAME":"Om","BIRTH DATE":'12/12/23'},
  {"NAME":"Rohan","BIRTH DATE":'30/01/22'},
  {"NAME":"Pratik","BIRTH DATE":'19/11/21'},
  {"NAME":"Suresh","BIRTH DATE":'29/03/20'},
  {"NAME":"Monu","BIRTH DATE":'10/04/25'},]
print(a)

Que-2]
#1. Write python code to find transpose and inverse of matrix
A =1 2 2
   2 1 2
   2 2 1
A=([[1,2,2],[2,1,2],[2,2,1]])
A.T
A.inv()

#2. Declare the matrix
A =5  2  5  4
   10 3  4  6
   2  0 −1  11
find a row echelon form and the rank of matrix A.

#3. Declare the matrix
A =2 −1 2 7
   4 7 3 4
   4 2 0 −1
find the matrices L and U such that A = LU.
