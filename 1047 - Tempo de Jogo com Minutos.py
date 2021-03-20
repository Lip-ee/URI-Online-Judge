values = [int(i) for i in input().split()]

hora_i = values[0]
minuto_i = values[1]
hora_f = values[2]
minuto_f = values[3]

hora_total = hora_f - hora_i

if hora_total < 0:
    hora_total += 24
    
minuto_total = minuto_f - minuto_i

if minuto_total < 0:
    minuto_total += 60
    hora_total -= 1
    if hora_total < 0:
        hora_total += 24
    
if minuto_total == 0 and hora_total == 0:
    print(f'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print(f'O JOGO DUROU {hora_total} HORA(S) E {minuto_total} MINUTO(S)')
