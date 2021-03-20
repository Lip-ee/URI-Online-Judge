# -*- coding: utf-8 -*-
values = input().split()

a = int(values[0])
b = int(values[1])

if a > b:
  if a % b == 0:
    print('Sao Multiplos')
  else:
    print('Nao sao Multiplos')
elif b > a:
  if b % a == 0:
    print('Sao Multiplos')
  else:
    print('Nao sao Multiplos')
else:
  print('Sao Multiplos')
