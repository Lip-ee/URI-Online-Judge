# -*- coding: utf-8 -*-
nums = input().split()

# ordem crescente
nums = list(map(int, nums)) 
# map() = transforma todos os itens da lista "nums" em inteiros iteráveis
cresc = sorted(nums)

for num in cresc:
  print(num)

# ordem normal (de acordo com o input)
print('')
for num in nums:
  print(num)