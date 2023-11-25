Slip No-8

Que-1]
1. Use Python code to find a + c,ab,cd,a/b and a(b + c),
where a = 5, b = 7, c = 9, d = 11.
a = 5
b = 7
c = 9
d = 11
print(a+c)
print(a*b)
print(c*d)
print(a/b)
print(a*(b+c))

2. The following two statements using the ‘+’string operation on Python.
a. string1 = India Won, string2 = World Cup
s1="India Won"
s2=" World Cup"
print(s1+s2)
  
b. string1 = God, string2 = is Great
s1="God"
s2=" is Great"
print(s1+s2)

3. Write Python code to find area and circumference of circle with radius 14.
r=float(input("Enter Radius:"))
a=3.14*r*r
c=2*3.14*r
print("Area Of Circle:",a)
print("Circumference Of Circle:",c)

1. Using Python code logically verify associativity of matrices with respective to matrix
addition (use proper matrices).

2. Write Python code to generate 10 terms of Fibonacci Sequence using loop.
a=0
b=1
print(a,b,end=" ")
for i in range(1,10):
    c=a+b
    a=b
    b=c
    print(c,end=" ")

3. Using Python code, find determinant and inverse of the matrix if exist.
A =4 2 2
   2 4 2
   2 2 4
A=Matrix([[4,2,2],[2,4,2],[2,2,4]])
A.det()
A.inv()
















