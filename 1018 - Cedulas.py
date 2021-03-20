# -*- coding: utf-8 -*-
din = int(input())

cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

print(din)

while (din != 0):
    if (din >= 100):
        din -= 100
        cem += 1
    elif (din >= 50):
        din -= 50
        cinquenta += 1
    elif (din >= 20):
        din -= 20
        vinte += 1
    elif (din >= 10):
        din -= 10
        dez += 1
    elif (din >= 5):
        din -= 5
        cinco += 1
    elif (din >= 2):
        din -= 2
        dois += 1
    elif (din >= 1):
        din -= 1
        um += 1

print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')