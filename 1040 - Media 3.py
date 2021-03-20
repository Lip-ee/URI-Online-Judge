# -*- coding: utf-8 -*-
notas = input().split()

n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])

med = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

if med >= 7:
  print(f'Media: {med:.1f}')
  print('Aluno aprovado.')
elif med < 5:
  print(f'Media: {med:.1f}')
  print('Aluno reprovado.')
elif med >= 5 and med < 7:
  print(f'Media: {med:.1f}')
  print('Aluno em exame.')

  nota_exame = float(input())
  print(f'Nota do exame: {nota_exame:.1f}')
  
  nova_med = (nota_exame + med) / 2
  
  if nova_med >= 5:
    print('Aluno aprovado.')
    print(f'Media final: {nova_med:.1f}')
  else:
    print('Aluno reprovado.')
    print(f'Media final: {nova_med:.1f}')