Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

z1 = 5+3*j
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    z1 = 5+3*j
NameError: name 'j' is not defined
z1 = (5+3j)
z2 = (-5+7j)
z1+z2
10j
z1-z2
(10-4j)
z1*z2
(-46+20j)

print("complex Number\n"*7)
complex Number
complex Number
complex Number
complex Number
complex Number
complex Number
complex Number

print("Real Number\n"*7)
Real Number
Real Number
Real Number
Real Number
Real Number
Real Number
Real Number

for i in range(1,51):
    print(i**3)

    
1
8
27
64
125
216
343
512
729
1000
1331
1728
2197
2744
3375
4096
4913
5832
6859
8000
9261
10648
12167
13824
15625
17576
19683
21952
24389
27000
29791
32768
35937
39304
42875
46656
50653
54872
59319
64000
68921
74088
79507
85184
91125
97336
103823
110592
117649
125000


from sympy import *
A = ones(10,10)
print(A)
Matrix([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
A.det()
0
A.trace()
10
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



def f(x):
    return x**3-4x-9
SyntaxError: invalid decimal literal
def f(x):
    return x**3-4*x-9

f(1)
-12
f(-1)
-6
f(0)
-9

from sympy import isprime
for i in range(500,1000):
    if isprime(i):
        print(i)

        
503
509
521
523
541
547
557
563
569
571
577
587
593
599
601
607
613
617
619
631
641
643
647
653
659
661
673
677
683
691
701
709
719
727
733
739
743
751
757
761
769
773
787
797
809
811
821
823
827
829
839
853
857
859
863
877
881
883
887
907
911
919
929
937
941
947
953
967
971
977
983
991
997
>>> 
>>> 
>>> def simpson13(f,a,b,n):
...     h=(b-a)/n
...     result = f(a)+f(b)
...     for i i range(1,n):
...         
SyntaxError: invalid syntax
>>> def simpson13(f,a,b,n):
...     h=(b-a)/n
...     result = f(a)+f(b)
...     for i in range(1,n):
...         if i%2==0:
...             result=result+2*f(a+i*h)
...         else:
...             result = result+4*f(a+i*h)
...             result = (h/3)*result
...             return result
... 
...         
>>> from math import *
>>> def f(x):
...     return sin(x)
... 
>>> simpson13(f,0,pi,6)
0.3490658503988659
