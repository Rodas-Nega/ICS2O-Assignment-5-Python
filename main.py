#!/usr/bin/ env python3

# Created By Rodas Nega
# Created On December 12 2020
# This program will calculate the circumference and area of a circle from given inputs 

import math

print('This program will calculate the circumference and area of your circle.')
print("")
radius = float(input('Enter your radius:'))
print("")
circumference = 2 * math.pi * radius
area = math.pi * radius**2
print('The circumference of your circle is %.2f' %circumference + 'mm')
print('The area of your circle is %.2f' %area + 'mm²')
print("")
if radius == 0:
  print('Radius cannot be a zero.')
elif radius <= 0:
  print('Radius cannot be negative.')
  