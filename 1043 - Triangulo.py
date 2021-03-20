# -*- coding: utf-8 -*-
values = input().split()

a = float(values[0])
b = float(values[1])
c = float(values[2])

cond1 = a < (b + c)
cond2 = b < (a + c)
cond3 = c < (b + a)

if cond1 and cond2 and cond3:
  perimetro = a + b + c
  print(f'Perimetro = {perimetro}')
else:
  area = ((a + b) * c) / 2
  print(f'Area = {area}')
