Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a =5
b=7
c=9
d=11
a+c
14
a*b
35
c**d
31381059609
a/b
0.7142857142857143
a(b+c)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a(b+c)
TypeError: 'int' object is not callable
a*(b+c)
80
print("India Won "+"World Cup")
India Won World Cup
print("God "+"is Great")
God is Great


r = 14
pi = 3.14
area = pi*r**2
print("Area of a circle is:: ",area)
Area of a circle is::  615.44
circum = 2*pi*r
print("Circumference of circle is:: ",circum)
Circumference of circle is::  87.92



nterms = int(input("How many terms? "))
How many terms? 10
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
...     while count < nterms:
...        print(n1)
...        nth = n1 + n2
...        # update values
...        n1 = n2
...        n2 = nth
...        count += 1
... 
...        
Fibonacci sequence:
0
1
1
2
3
5
8
13
21
34
>>> 
>>> from sympy import *
>>> A = Matrix([[4,2,2],[2,4,2],[2,2,4]])
>>> print(A)
Matrix([[4, 2, 2], [2, 4, 2], [2, 2, 4]])
>>> A.det()
32
>>> A**-1
Matrix([
[ 3/8, -1/8, -1/8],
[-1/8,  3/8, -1/8],
[-1/8, -1/8,  3/8]])
>>> A.inv()
Matrix([
[ 3/8, -1/8, -1/8],
[-1/8,  3/8, -1/8],
[-1/8, -1/8,  3/8]])
>>> 
>>> 
