# -*- coding: utf-8 -*-
XY1_Values = input()
XY2_Values = input()

list_XY1_Values = XY1_Values.split()
list_XY2_Values = XY2_Values.split()

x1 = float(list_XY1_Values[0])
y1 = float(list_XY1_Values[1])

x2 = float(list_XY2_Values[0])
y2 = float(list_XY2_Values[1])

dist = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

print(f'{dist:.4f}')