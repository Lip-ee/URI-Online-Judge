# -*- coding: utf-8 -*-
valor = float(input())

# listas com as notas e moedas
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
# pra cada nota na lista "notas"
for nota in notas:
    # dividimos o valor pela nota = quantas notas necessárias
    qt_notas = int(valor / nota) 
    # mostramos quantas e quais notas serão utilizadas
    print('{} nota(s) de R$ {:.2f}'.format(qt_notas, nota))
    # subtramímos o produto entre as notas necessárias com a nota atual do looping e armazenamos dentro do valor novamente
    valor -= qt_notas * nota
    

print('MOEDAS:')
# pra cara moeda na lista "moedas"
for moeda in moedas:
    # arredondamos o valor com 2 casas decimais
    valor = round(valor, 2)
    # dividimos o valor pela moeda = quantas moedas necessárias
    qt_moedas = int(valor / moeda)
    # mostramos quantas e quais moedas serão utilizadas
    print('{} moeda(s) de R$ {:.2f}'.format(qt_moedas, moeda))
    # subtramímos o produto entre as moedas necessárias com a moeda atual do looping e armazenamos dentro do valor novamente
    valor -= qt_moedas * moeda
