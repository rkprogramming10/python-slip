Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def simpson(f,a,b,n):
	h=(b-a)/n
	result = f(a)+f(b)
	for i in range(1,n):
		if i%2==0:
			result = result+2*f(a+i*h)
		else:
			result = result+4*f(a+i+h)
			result = (h/3)*result
			return result

		
>>> from math import *
>>> def f(x):
	return(x)

>>> simpson(f,0,pi,6)
1.6119839601578574
>>> 
================================ RESTART: Shell ================================
>>> import numpy as np
>>> n = int(input('Enter the number of data points:: '))
Enter the number of data points:: 4
>>> x = np.zeros((n))
>>> y = np.zeros((n))
SyntaxError: multiple statements found while compiling a single statement
>>> 
================================ RESTART: Shell ================================
>>> import numpy as np
>>> n = int(input('Enter the number of data points:: '))
Enter the number of data points:: 4
>>> x = np.zeros((n))
>>> y = np.zeros((n))
>>> print('Enter data for x and y:: ')
Enter data for x and y:: 
>>> for i in range(n):
	x[i] = float(input('x['+str(i)+']='))
	y[i] = float(input('y['+str(i)+']='))
	xp = float(input("enter interpolation"))
	yp = 0
	for i in range(n):
		p=1
		for j in range(n):
			if i !=j:
				p = p*(xp-x[j])/(x[i]-x[j])
				yp = yp + p*y[i]
				print('Interpolated value at %.3f is %.3f' %(xp,yp))

				
x[0]=0
y[0]=5
enter interpolation3

Warning (from warnings module):
  File "<pyshell#15>", line 10
RuntimeWarning: divide by zero encountered in scalar divide
Interpolated value at 3.000 is inf
Interpolated value at 3.000 is inf
Interpolated value at 3.000 is inf

Warning (from warnings module):
  File "<pyshell#15>", line 11
RuntimeWarning: invalid value encountered in scalar multiply
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
x[1]=1
y[1]=133
enter interpolation3
Interpolated value at 3.000 is -10.000
Interpolated value at 3.000 is -inf
Interpolated value at 3.000 is -inf
Interpolated value at 3.000 is -inf
Interpolated value at 3.000 is -inf
Interpolated value at 3.000 is -inf
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
x[2]=2
y[2]=22
enter interpolation3
Interpolated value at 3.000 is -10.000
Interpolated value at 3.000 is -5.000
Interpolated value at 3.000 is inf
Interpolated value at 3.000 is inf
Interpolated value at 3.000 is inf
Interpolated value at 3.000 is inf
Interpolated value at 3.000 is inf
Interpolated value at 3.000 is inf
Interpolated value at 3.000 is inf
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
Interpolated value at 3.000 is nan
x[3]=5
y[3]=129
enter interpolation3
Interpolated value at 3.000 is -10.000
Interpolated value at 3.000 is -5.000
Interpolated value at 3.000 is -3.000
Interpolated value at 3.000 is 396.000
Interpolated value at 3.000 is -3.000
Interpolated value at 3.000 is -202.500
Interpolated value at 3.000 is -169.500
Interpolated value at 3.000 is -103.500
Interpolated value at 3.000 is -59.500
Interpolated value at 3.000 is 17.900
Interpolated value at 3.000 is 56.600
Interpolated value at 3.000 is 69.500
>>> 
================================ RESTART: Shell ================================
>>> def trapizoidal(f,a,b,n):
	h=(b-a)/n
	result=f(a)+f(b)
	for i in range(1,n):
		result=result+2*f(a+i*h)
		result=(h/2)*result
		return result

	
>>> 
>>> from math import *
>>> def f(x):
	return sin(x)

>>> trapizoidal(f,0,pi,8)
0.15027943247108658
>>> 
