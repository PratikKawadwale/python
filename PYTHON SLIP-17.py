Slip No-17

#1. Write the Python code to print ‘Python is bad’ and ‘Python is wonderful’ , where
wonderful is global variable and bad is local variable.


#2. Write Python code to evaluate eigen value and eigen vector of the following matrix.
A =1 1 1
   0 1 1
   0 0 1
A=Matrix([[1,1,1],[0,1,1],[0,0,1]])
A.eigenvals()
A.eigenvects()


#3.Write Python code,find a,b and c such that a^2 + b^2=c^2.(where 1 ≤ a, b, c ≤ 50)

Que-2]
#1. Using Python code construct any two matrices A and B to show that (AB)^−1 = B^−1 A^−1.

2. Use linsolve code in python to solve the following system of linear equations.
x − 2y + 3z = 7
2x + y + z = 4
−3x + 2y − 2z = −10
A=Matrix([[1,-2,3],[2,1,1],[-3,2,-2]])
B=Matrix([[7,4,-10]])
linsolve((A,B))

3. Write python code to find trace and transpose of the matrix
1 3 3
2 2 3
4 2 1

A.T=([[1,3,3],[2,2,3],[4,2,1]])








