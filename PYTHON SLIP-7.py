Slip No-7
1. Using Python, evaluate the following expression of two complex number
z1 = 5 + 3j and z2 = −5 + 7j.

z1 = 5 + 3j
z2 = -5 + 7j
a. z1 + z2
print(z1+z2)

b. z1 − z2
print(z1-z2)

c. z1 ∗ z2
print(z1*z2)

2. Repeat the following string 7 times using the string operator ‘*’ on Python.
a. Complex Number
a="Complex Number"
print(a*7)

b. Real Number
a="Real Number"
print(a*7)

3. Write Python code to generate cube of numbers from 1 to 50.
for i in range(1,51):
    print("Cube of",i,"=",i*i*i)

Que-2]
1. Using Python code construct 0nes matrix of order 10 × 10 and hence find determinant, trace and transpose of it.

2. Write Python code to obtained f(−1), f(0), f(1) of the f(x) = x^3 − 4x − 9.
    
3. Generate all the prime numbers between 500 to 1000 using Python program.
def prime(n):
  f=0
  for i in range(2,n):
    if n%i==0:
      f=1
      break
  if f==0:
    print(n, end=" ")
for i in range(500,1000):
  prime(i)










