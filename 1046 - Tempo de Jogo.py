# -*- coding: utf-8 -*-
values = map(int,input().split())
start, end = list(values)

if (start < end):
    time = end - start
else:
    time = end + 24 - start

print(f'O JOGO DUROU {time} HORA(S)')