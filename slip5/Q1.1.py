Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> radius = 7
>>> pi = 3.14
>>> volume = (4.0/3.0)*pi*(radius**3)
>>> print('volume of the sphere= ' +str(volume))
volume of the sphere= 1436.0266666666666
>>>
================================ RESTART: Shell ================================
>>> n=int(input("Enter a number: "))
Enter a number: 30
>>> sum1 = 0
>>> while(n > 0):
    sum1=sum1+n
    n=n-1
    print('the sum of first n natural number is:: ',sum1)

    
the sum of first n natural number is::  30
the sum of first n natural number is::  59
the sum of first n natural number is::  87
the sum of first n natural number is::  114
the sum of first n natural number is::  140
the sum of first n natural number is::  165
the sum of first n natural number is::  189
the sum of first n natural number is::  212
the sum of first n natural number is::  234
the sum of first n natural number is::  255
the sum of first n natural number is::  275
the sum of first n natural number is::  294
the sum of first n natural number is::  312
the sum of first n natural number is::  329
the sum of first n natural number is::  345
the sum of first n natural number is::  360
the sum of first n natural number is::  374
the sum of first n natural number is::  387
the sum of first n natural number is::  399
the sum of first n natural number is::  410
the sum of first n natural number is::  420
the sum of first n natural number is::  429
the sum of first n natural number is::  437
the sum of first n natural number is::  444
the sum of first n natural number is::  450
the sum of first n natural number is::  455
the sum of first n natural number is::  459
the sum of first n natural number is::  462
the sum of first n natural number is::  464
the sum of first n natural number is::  465
>>> 
>>> str1 = 'hello'
>>> str2 ='world'
>>> print(str1+str2)
helloworld
>>> str3 = 'good '
>>> str4 = 'morning'
>>> print(str3 + str4)
good morning
>>> for i in range(20,30):
	print('Square from 20 to 30 is\n',i**2)

	
Square from 20 to 30 is
 400
Square from 20 to 30 is
 441
Square from 20 to 30 is
 484
Square from 20 to 30 is
 529
Square from 20 to 30 is
 576
Square from 20 to 30 is
 625
Square from 20 to 30 is
 676
Square from 20 to 30 is
 729
Square from 20 to 30 is
 784
Square from 20 to 30 is
 841
>>> 
>>> 
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
>>> 

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
>>> def simpson38(f,a,b,n):
	h=(b-a)/n
	result = f(a)+f(b)
	for i in range(1,n):
		if i%3==0:
			result = result+2*f(a+i*h)
		else:
			result=result+3*f(a+i*h)
			result=((3*h/8))*result
			return result

		
>>> from math import *
>>> def f(x):
	return sin(x)

>>> simpson38(f,0,pi,6)
0.2945243112740431
>>> 
>>> 
>>> print("option","3.a.2")
option 3.a.2
>>> 
>>> def trapizoidal(f,a,b,n):
	h=(b-a)/n
	result=f(a)+f(b)
	for i in range(1,n):
		result=result+2*f(a+i*h)
		result=(h/2)*result
		return result

	
>>> from math import *
>>> def f(x):
	return sin(x)

>>> trapizoidal(f,0,pi,5)
0.36931636609809143
>>> 
================================ RESTART: Shell ================================
>>> from sympy import *
>>> A = Matrix([[-1,1,0],[8,5,2],[2,-6,2]])
>>> B = Matrix([[9,0,3],[1,4,1],[1,0,-1]])
>>> 2*A+B
Matrix([
[ 7,   2, 3],
[17,  14, 5],
[ 5, -12, 3]])
>>> 3*A-5*B
Matrix([
[-48,   3, -15],
[ 19,  -5,   1],
[  1, -18,  11]])
>>> A**-1
Matrix([
[-11/17, 1/17, -1/17],
[  6/17, 1/17, -1/17],
[ 29/17, 2/17, 13/34]])
>>> B**3
Matrix([
[780,  0, 228],
[148, 64,  52],
[ 76,  0,  20]])

>>> A.T+B.T
Matrix([
[8, 9,  3],
[1, 9, -6],
[3, 3,  1]])
>>> 
>>> 
>>> 
>>> M = [1,2,3,4]

>>> len(M)
4
>>> L = "XYZ" + "pqr"
>>> print(L)
XYZpqr
>>> s = 'Make In India'
>>> (s[:7])
'Make In'
>>> (s[:9])
'Make In I'
>>> 
>>> 
>>> for i in range(21,49):
	print(i**2)

	
441
484
529
576
625
676
729
784
841
900
961
1024
1089
1156
1225
1296
1369
1444
1521
1600
1681
1764
1849
1936
2025
2116
2209
2304

>>> import cmath
>>> for i in range(21,49):
	cmath.sqrt(i)

	
(4.58257569495584+0j)
(4.69041575982343+0j)
(4.795831523312719+0j)
(4.898979485566356+0j)
(5+0j)
(5.0990195135927845+0j)
(5.196152422706632+0j)
(5.291502622129181+0j)
(5.385164807134504+0j)
(5.477225575051661+0j)
(5.5677643628300215+0j)
(5.656854249492381+0j)
(5.744562646538029+0j)
(5.830951894845301+0j)
(5.916079783099616+0j)
(6+0j)
(6.082762530298219+0j)
(6.164414002968976+0j)
(6.244997998398398+0j)
(6.324555320336759+0j)
(6.4031242374328485+0j)
(6.48074069840786+0j)
(6.557438524302+0j)
(6.6332495807108+0j)
(6.708203932499369+0j)
(6.782329983125268+0j)
(6.855654600401044+0j)
(6.928203230275509+0j)
>>> 
>>> 
>>> 