# -*- coding: utf-8 -*-
name = str(input())
salary = float(input())
tVendas = float(input())

fSalary = (tVendas * 0.15) + salary

print(f'TOTAL = R$ {fSalary:.2f}')