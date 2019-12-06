import math as m




## First Image

b = 0.35

h = 0.15


A = (b*h)/2
Xc = (2*b)/3
Yc = h/3

Ixc = (b*(h**3))/36

Iyc = (h*(b**3))/36 

Ic = (b*(h**3))/12

Iy = (h*(b**3))/4


print(A, Xc, Yc, Ixc, Iyc, Ic, Iy)


## Second Image
b = 0.7
h = 0.2


A = (b*h)/2
Xc = b/3
Yc = h/3

Ixc = (b*(h**3))/36

Iyc = (h*(b**3))/36 

Ic = (b*(h**3))/12

Iy = (h*(b**3))/12

print(A, Xc, Yc, Ixc, Iyc, Ic, Iy)


# Third Image

a = 1.5
b = 2.2
h = 1.5


A = (b*h)/2
Xc = (a+ b)/3
Yc = h/3

Ixc = (b*(h**3))/36

Iyc = ((b*h)*((b**2) -(a*b) + (a**2)))/36

Ic = (b*(h**3))/12

Iy = ((b*h)*((b**2) +(a*b) + (a**2)))/12

print(A, Xc, Yc, Ixc, Iyc, Ic, Iy)

#Fourth Figure

b = 3.0
h = 5.0


A = (b*h)
Xc = b/2
Yc = h/2

Ixc = (b*(h**3))/12

Iyc = (h*(b**3))/12 

Ic = (b*(h**3))/3

Iy = (h*(b**3))/3

J = ((b*h)*((b**2) + (h**2)))/12

print(A, Xc, Yc, Ixc, Iyc, Ic, Iy, J)



# Fifth Figure

a = 1.5
b = 2.5
theta = m.radians(45) 

A = a * b * m.sin(theta)
Xc = (b + (a*m.cos(theta)))/2
Yc = (a * m.sin(theta))/2

Ixc = (a**3 *b * (m.sin(theta)**3))/12
Iyc = (a*b*m.sin(theta)*(b**2 + (a**2*m.cos(theta)**2)))/12

Ix = (a**3 *b * (m.sin(theta)**3))/3
Iy = ((a*b*m.sin(theta)*(b + (a*m.cos(theta))**2))/3) - (a**2 * b**2 * m.sin(theta)* m.cos(theta))

print(A, Xc, Yc, Ixc, Iyc, Ic, Iy)



#PAGE 2 Circle Stuff
## First Image
a = 1.2

A = m.pi()*a**2
Xc = a
Yc = a

Ixc = (m.pi()*a**4)/4

Iyc = (m.pi()*a**4)/4 

Ic = (5*m.pi()*a**4)/4

Iy = (5*m.pi()*a**4)/4

J = (m.pi()*a**4)/2

print(A, Xc, Yc, Ixc, Iyc, Ic, Iy, J)



## Second Image
a = 3.1
b= 3.0

A = m.pi()*(a**2 - b**2)
Xc = a
Yc = a

Ixc = (m.pi()*(a**4 - b**4))/4

Iyc = (m.pi()*(a**4 - b**4))/4 

Ic = ((5*m.pi()*a**4)/4) - (m.pi()*a**2*b**2) - ((m.pi()*b**4)/4) 

Iy = ((5*m.pi()*a**4)/4) - (m.pi()*a**2*b**2) - ((m.pi()*b**4)/4)

J = (m.pi()*(a**4-b**4))/2

print(A, Xc, Yc, Ixc, Iyc, Ic, Iy, J)


## Third Image
a = 0.75


A = (m.pi()*a**2)/2
Xc = a
Yc = (4*a)/(3*m.pi())

Ixc = (a**4*(9*m.pi()**2 - 64))/(72*m.pi())

Iyc = (m.pi()*a**4)/8 

Ic = (m.pi()*a**4)/8 

Iy = (5*m.pi()*a**4)/8


print(A, Xc, Yc, Ixc, Iyc, Ic, Iy)



## Fourth Image
a = 0.6
theta = m.radians(30)

A = a**2*theta
Xc = ((2*a)/3)*(m.sin(theta)/theta)
Yc = 0

Ic = (a**4*(theta - m.sin(theta)*m.cos(theta)))/4 

Iy = (a**4*(theta + m.sin(theta)*m.cos(theta)))/4


print(A, Xc, Yc, Ic, Iy)


## Fifth Image
a = 0.45
theta = m.radians(17.5)

A = a**2*(theta - (m.sin(2*theta)/2))

Xc = ((2*a)/3)*((m.sin(theta)**3)/(theta - (m.sin(theta)*m.cos(theta))))

Yc = 0

Ic = (A*a**2/4)*(1-((2*m.sin(theta)**3*cos(theta))/((3*theta)-(3*m.sin(theta)*m.cos(theta))))) 

Iy = (A*a**2/4)*(1-((2*m.sin(theta)**3*cos(theta))/((theta)-(3*m.sin(theta)*m.cos(theta))))) 

print(A, Xc, Yc, Ic, Iy)


#SHEET 3
#Diagram 1

a = 1.4
b = 0.15

A = (4*a*b)/3
Xc = (3*a)/5
Yc = 0

Ixc = (4*a*b**2)/15

Iyc = (16*a**3*b)/175

Ix = Ixc

Iy = (4*a**3*b)/7

#  Diagram 2

a = 2.75
b = 0.35

A = (2*a*b)/3
Xc = (3*a)/5
Yc = (3*b)/8

Ix = (2*a*b**2)/15

Iy = (2*a**3*b)/7

# Diagram 3










