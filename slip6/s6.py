Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
23%2+9-(3+7)*10/2
-40.0
35*10//3+15%3
116
3**5-2**5+4//7
211
x = [7,8,71,32,49,-5,7,7,0,1,6]
min(x)
-5
max(x)
71
ones(10,10)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ones(10,10)
NameError: name 'ones' is not defined
from sympy import *
ones(10,10)
Matrix([
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
A= ones(10,10)
print(A)
Matrix([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
A.det()
0
A.trace()
10
A.transpose
<bound method MatrixOperations.transpose of Matrix([
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])>
A.T
Matrix([
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

def f(x,y):
    return x**2-2*x*y+4

f(2,0)
8
f(1,-1)
7


for i in range(1,201):
    if i%7==0:
        print(i)

        
7
14
21
28
35
42
49
56
63
70
77
84
91
98
105
112
119
126
133
140
147
154
161
168
175
182
189
196


def simpson13(f,a,b,n):
    h=(b-a)/n
    result = f(a)+f(b)
...     for i in range(1,n):
...         if i%2==0
...         
SyntaxError: incomplete input
>>> def simpson13(f,a,b,n):
...     h=(b-a)/n
...     result = f(a)+f(b)
...     for i in range(1,n):
...         if i%2==0:
...             result = result+2*f(a+i*h)
...         else:
...             result+4*f(a+i*h)
...             result = (h/3)*result
...             return result
... 
...         
>>> from math import *
>>> def f(x):
...     return sin(x)
... 
>>> simpson13(f,0,pi,5)
2.5648942582957196e-17
>>> 
>>> 
>>> def trapizoidal(f,a,b,n):
...     h=(b-a)/n
...     result = f(a)+f(b)
...     for i in range(1,n):
...         result = result+2*f(a+i*h)
...         result = (h/2)*result
...         return result
... 
...     
>>> from math import *
>>> def f(x):
...     return sin(x)
... 
>>> trapizoidal(f,0,pi,10)
0.09708055193627334
