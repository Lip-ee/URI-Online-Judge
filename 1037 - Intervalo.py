# -*- coding: utf-8 -*-
num = float(input())

if 0 <= num <= 25:
  print('Intervalo [0,25]')

if 25 < num <= 50:
  print('Intervalo (25,50]')

if 50 < num <= 75:
  print('Intervalo (50,75]')

if 75 < num <= 100:
  print('Intervalo (75,100]')

if num < 0 or num > 100:
  print('Fora de intervalo')