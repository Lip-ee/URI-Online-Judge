# -*- coding: utf-8 -*-
# pc = cod, qtd, valor

PC1 = input()
PC2 = input()

listPC1 = PC1.split()
listPC2 = PC2.split()

tValPC1 = int(listPC1[1]) * float(listPC1[2])
tValPC2 = int(listPC2[1]) * float(listPC2[2])

fTotal = tValPC1 + tValPC2

print(f'VALOR A PAGAR: R$ {fTotal:.2f}')
