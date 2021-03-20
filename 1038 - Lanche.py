# -*- coding: utf-8 -*-
pedidos = input()

lista_pedidos = pedidos.split()

id_prod = int(lista_pedidos[0])
qtd_prod = int(lista_pedidos[1])

total = 0

if (id_prod == 1):
  total = qtd_prod * 4.00
elif (id_prod == 2):
  total = qtd_prod * 4.50
elif (id_prod == 3):
  total = qtd_prod * 5.00
elif (id_prod == 4):
  total = qtd_prod * 2.00
elif (id_prod == 5):
  total = qtd_prod * 1.50

print(f'Total: R$ {total:.2f}')
