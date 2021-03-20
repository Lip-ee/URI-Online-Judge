# -*- coding: utf-8 -*-
tempo = int(input())

anos = tempo // 365
dias_rest = tempo % 365

meses = dias_rest // 30
dias_rest = dias_rest % 30

print(f'{anos} ano(s)\n{meses} mes(es)\n{dias_rest} dia(s)')