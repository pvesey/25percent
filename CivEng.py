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


