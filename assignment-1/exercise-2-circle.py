from math import pi
r = float(input('Enter the Radius of Circle: '))
while r <= 0:
    r = float(input('Insert Positive Number for Radius: '))
p = 2*pi*r
a = pi*r**2
print('Primeter: ', p, '\nArea: ', a)
