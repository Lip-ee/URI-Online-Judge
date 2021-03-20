# -*- coding: utf-8 -*-
# Se B > C and D > A and C + D > A + B and C >= 0 and D >= 0 and A % 2 == 0:

numbers = input()

list_nums = numbers.split()

A = int(list_nums[0])
B = int(list_nums[1])
C = int(list_nums[2])
D = int(list_nums[3])

if B > C and D > A and C + D > A + B and C >= 0 and D >= 0 and A % 2 == 0:
  print('Valores aceitos')
else:
  print('Valores nao aceitos')