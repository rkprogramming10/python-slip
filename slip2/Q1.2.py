Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f(x):
	return x**3+5*x+6

>>> f(-2)
-12
>>> f(0)
6
>>> f(2)
24
>>> def f(x):
	return x**3+5*x

>>> f(10)
1050
>>> 
>>> from sympy import *
>>> a = Matrix([[4,2,2],[2,4,2],[2,2,4]])
>>> a.eigenvals()
{8: 1, 2: 2}
>>> a.eigenvects()
[(2, 2, [Matrix([
[-1],
[ 1],
[ 0]]), Matrix([
[-1],
[ 0],
[ 1]])]), (8, 1, [Matrix([
[1],
[1],
[1]])])]
>>> 
