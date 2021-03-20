# -*- coding: utf-8 -*-
values = input().split()

values = list(map(float, values))
values = sorted(values, reverse=True)

a = values[0]
b = values[1]
c = values[2]

ret = a ** 2 == b ** 2 + c ** 2
obt = (a ** 2) > (b ** 2 + c ** 2)
acu = a ** 2 < b ** 2 + c ** 2
equi = a == b == c
iso = a == b != c or a == c != b or b == c != a
naotri = a >= (b + c)

if ret:
  print('TRIANGULO RETANGULO')
if obt and not naotri:
  print('TRIANGULO OBTUSANGULO')
if acu:
  print('TRIANGULO ACUTANGULO')
if equi:
  print('TRIANGULO EQUILATERO')
if iso:
  print('TRIANGULO ISOSCELES')
if naotri:
  print('NAO FORMA TRIANGULO')