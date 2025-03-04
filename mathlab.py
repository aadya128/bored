#1. finding rank of a matrix
#a. 
'''import numpy as np
mx=np.array([[1,2,3,2],[2,3,5,1],[1,3,4,5]])
R=np.linalg.matrix_rank(mx)
print(mx)
print('rank of thematrix is: ',R)

#b
import numpy as np
mx = np.array([[1,1,1],[0,1,2],[1,5,3]])
R = np.linalg.matrix_rank(mx)
print(mx)
print('the rank of the matrix: ',R)

#2. solution of system of linear equations using gauss seidel method
#a
f1 = lambda x,y,z:(12-y-z)/10
f2 = lambda x,y,z:(12-x-z)/10
f3 = lambda x,y,z:(12-y-z)/10
x0=0
y0=0
z0=0
x1 = f1(x0,y0,z0)
y1 = f2(x1,y0,z0)
z1 = f3(x1,y1,z0)
print("\n1: x1=%0.4f, y1=%0.4f, z1=%0.4f\n" %(x1,y1,z1))
x2 = f1(x1,y1,z1)
y2 = f2(x2,y1,z1)
z2 = f3(x2,y2,z1)
print("\n2: x2=%0.4f, y2=%0.4f, z2=%0.4f\n" %(x2,y2,z2))
x3 = f1(x2,y2,z2)
y3 = f2(x3,y2,z2)
z3 = f3(x3,y3,z2)
print("\n3: x3=%0.4f, y3=%0.4f, z3=%0.4f\n" %(x3,y3,z3))
print("\nsolution : x=%0.3f, y=%0.3f and z2=%0.3f\n" %(x3,y3,z3))

#b.
f1 = lambda x,y,z:(8-y-z)/10
f2 = lambda x,y,z:(8-x-z)/10
f3 = lambda x,y,z:(8-y-x)/10
x0=0
y0=0
z0=0
x1 = f1(x0,y0,z0)
y1 = f2(x1,y0,z0)
z1 = f3(x1,y1,z0)
print("\n 1 : x1=%0.4f, y1=%0.4f, z1=%0.4f\n" %(x1,y1,z1))
x2 = f1(x1,y1,z1)
y2 = f2(x2,y1,z1)
z2 = f3(x2,y2,z1)
print("\n 2 : x2=%0.4f, y2=%0.4f, z2=%0.4f\n" %(x2,y2,z2))
x3 = f1(x2,y2,z2)
y3 = f2(x3,y2,z2)
z3 = f3(x3,y3,z2)
print("\n 3 : x3=%0.4f, y3=%0.4f, z3=%0.4f\n" %(x3,y3,z3))
print("\nsolution : x=%0.3f,y=%0.3f,z2=%0.3f" %(x3,y3,z3))'

#3. find the eigen values and eigen vectors for square matrix
#a
from sympy import *
A = Matrix([[5,4],[1,2]])
print('the given matrix is A: ', A)
eigen_values = A.eigenvals()
eigen_vectors = A.eigenvects()
print('eigen values: ', eigen_values)
print('eigen vectors: ', eigen_vectors)

#b
from sympy import *
A = Matrix([[2,0,1],[0,2,0],[1,0,2]])
print(A)
eigen_values = A.eigenvals()
eigen_vectors = A.eigenvects()
print('eigen values: ', eigen_values)
print('eigen vectors: ', eigen_vectors)

#4. find the largest and smallest eigen value by rayleigh power method
#a.
import numpy as np
def normalize(x):
    fac = abs(x).max()
    x_n = x/x.max()
    return fac,x_n
x=np.array([1,1,1])
a=np.array([[1,1,3],[1,5,1],[3,1,1]])
for i in range(10):
    x=np.dot(a,x)
    lambda_1,x=normalize(x)
print('eigenvalue: ', lambda_1)
print('eigenvector: ',x)

#b.
import numpy as np
def normalize(x):
    fac = abs(x).max()
    x_n = x/x.max()
    return fac,x_n
x=np.array([1,1,1])
a=np.array([[6,-2,2],[-2,3,-1],[-2,-1,3]])
for i in range(10):
    x=np.dot(a,x)
    lambda_1,x=normalize(x)
print('eigenvalue: ', lambda_1)
print('eigenvector: ',x)

#5. find the angle between radius vector and tangent 
#a.
from sympy import *
a,t = symbols('a,t')
R = a*(1+cos(t))
dRdt = diff(R,t)
R = R.subs(t,pi/6)
dRdt = dRdt.subs(t,pi/6)
PHI = atan(R/dRdt)
print('the angle between the radius vector and tangest is: ',PHI)
if PHI<0:
    PHI = PHI+pi
print('the angle between radius vector and tangent: ', PHI)

#b.
from sympy import *
a,t = symbols('a,t')
R=2*a/(1-cos(t))
dRdt=diff(R,t)
R=R.subs(t,2*pi/3)
dRdt=dRdt.subs(t,2*pi/3)
PHI = atan(R/dRdt)
print('angle is: ', PHI)
if PHI<0:
    PHI = PHI+pi
print('the angle is: ',PHI)

#6. find the radius of curvature in cartesian and polar form
#a.
from sympy import *
x,y,c=symbols('x,y,c')
y = c**2/x
y1 = diff(y,x)
y2 = diff(y,x,2)
roh=(1+y1**2)**(3/2)/y2
print('radius of curvature is: ',roh)


#b.
from sympy import *
r = a*(t+sint)
r1 = diff(r,t)
r2 = diff(r1,t)
roh=simplify((r**2+r1**2)**(3/2)/r**2+2**r1**2-r*r2)
roh = simplify(roh.subst,0)
print('roc: ',roh)

#c.
#d.


#7. find partiall derivatives
#a.
from sympy import *
x,y,z =symbols('x,y,z')
f = 4*x*y + x*sin(z) + x**3 + z**8*y
print(f)
fx = diff(f,x)
fy = diff(f,y)
fz = diff(f,z)
print('partial derivtive wrt x = ', fx)
print('partial derivtive wrt y = ', fy)
print('partial derivtive wrt z = ', fz)

#b.
from sympy import *
x,y,a = symbols('x,y,a')
f = x**3 + y**3 - 3*a*x*y
print(f)
fx = diff(f,x)
fy = diff(f,y)
fxx = diff(f,x,x)
fyy = diff(f,y,y)
fxy = diff(f,x,y)
print('partial derivtive wrt x = ', fx)
print('partial derivtive wrt y = ', fy)
print('partial derivtive wrt xx = ', fxx)
print('partial derivtive wrt yy = ', fyy)
print('partial derivtive wrt xy = ', fxy)

#8. find the jacobian
#a.
from sympy import *
x,y = symbols('x,y')
u=x*(1-y)
v=x*y
A = Matrix([u,v])
jacA = A.jacobian([x,y])
jacobian = simplify(det(jacA))
print(jacobian)

#b.
from sympy import *
x,y=symbols('x,y')
u=2*x*y
v=x**2 - y**2
A = Matrix([u,v])
jacA = A.jacobian([x,y])
jacobian = simplify(det(jacA))
print(jacobian)

#9. fiind gcd using euclids theorem
#a.
def gcd1(a,b):
    c=1
    if b<a:
        a,b=b,a
    while (c>0):
        c=b%a
        print(a,c)
        b=a
        a=c
        continue
    print(b)
gcd1(25520,19314)

#10.solving linear congruencies
#a.
from sympy import *
a = int(input('enter a: '))
b = int(input('enter b: '))
m = int(input('enter m: '))
d=gcd(a,m)
if (b%d!=0):
    print('congruence has no soln')
else:
    for i in range(1,m-1):
        x=(m/a)*i+(b/a)
        if (x//1==x):
            print(x)
            break


#1,4 -- numpy
#2,9 -- None
#rest -- sympy

from sympy import *
a=5
b=3
m=13
d=gcd(a,m)
if b%d!=0:
    print('no soln')
else: 
    for i in range(1,m-1):
        x = (m/a)*i + (b/a)
        if (x//1==x):
            print(x)
'''