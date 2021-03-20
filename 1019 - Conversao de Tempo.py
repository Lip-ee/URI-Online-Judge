# -*- coding: utf-8 -*-
# tempo = total de segundos
tempo = int(input())

# horas = segundos (tempo) divididos (sem resto) por 3600
horas = tempo // 3600
segundos_rest = tempo % 3600
'''
segundos_restantes:
módulo da divisão dos segundos totais (tempo) por 3600
'''

# minutos = segundos_restantes divididos (sem resto) por 60
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60
'''
segundos_restantes:
módulo da divisão dos segundos_restantes (sem resto) por 60
'''

print(f'{horas:.0f}:{minutos:.0f}:{segundos_rest:.0f}')