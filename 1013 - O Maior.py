# -*- coding: utf-8 -*-
values = input()

lValues = values.split()

a = float(lValues[0])
b = float(lValues[1])
c = float(lValues[2])

maiorAB = (a + b + abs(a - b)) / 2
maiorABC = (maiorAB + c + abs(maiorAB - c)) / 2

print(f'{maiorABC:.0f} eh o maior')