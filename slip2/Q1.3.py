Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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
