SLIP NO-2

1.Write Python code to calculate the volume of a sphere with radius r=7(V=4/3πr**3).
r=7
v=4/3*3.14*r**3
print("Volume of Sphere",v)

2. Use Python code to construct string operation ‘+’ below string.
a. string1 = Hello, string2 = World!
s1="Hello"
s2="World!"
print(s1+s2)

b. string1 = Good, string2 = Morning
s1="Good"
s2="Morning"
print(s1+s2)

3. Write Python code to generate the square of numbers from 20 to 30.
for i in range(20,31):
    print(i,"square=",i*i)

Que-2]
1.Use python code find value of f(−2),f(0),f(2) where f(x)= x**2–5x+6.
def f(x):
    return x**2-5*x+6
print(f(-2),end=" ")
print(f(0),end=" ")
print(f(2),end=" ")

2.Write Python program to find the 10 term of the sequence of function f(x)=x**3+5x.
def f(x):
    return x**3+5*x
for x in range(1,11):
    print(f(x),end=" ")

3. Using sympy module of python, find the eigenvalues and corresponding eigenvectors
of the matrix A = 4 2 2
                  2 4 2
                  2 2 4

from sympy import*
A=Matrix([[4,2,2],[2,4,2],[2,2,4]])
A.eigenvals()
A.eigenvects()
