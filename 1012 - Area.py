# -*- coding: utf-8 -*-
values = input()

lValues = values.split()

a = float(lValues[0])
b = float(lValues[1])
c = float(lValues[2])

triangulo = a * c / 2
circulo = 3.14159 * (c ** 2)
trapezio = ((a + b) * c) / 2
quadrado = b * b
retangulo = a * b

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')