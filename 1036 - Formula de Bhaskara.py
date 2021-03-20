# -*- coding: utf-8 -*-
# input já fatiado com os valores float sendo atribuidos às variáveis a, b, c
a, b, c = [float(x) for x in input().split()]

delta = b ** 2 - 4 * a * c

if delta < 0 or a == 0.0:
  print('Impossivel calcular')
else:
  r1 = (-b + (delta ** (1/2))) / (2 * a)
  r2 = (-b - (delta ** (1/2))) / (2 * a)
  print(f'R1 = {r1:.5f}\nR2 = {r2:.5f}')
