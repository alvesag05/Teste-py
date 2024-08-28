                    #Ordem de precedencia
# + = addição
# - = subtração
# * = multiplicar
# / = divisão
# ** = potência
# // = divisão inteira
# % = resto da divisão

#5 + 2 == 7 
#5 - 2 == 3
#5 * 2 == 10
#5 / 2 == 2.5
#5 ** 2 == 25
#5 // 2 == 2
#5 % 2 == 1

#1 () para expressões aritimeticas
#2 ** segunda coisa importante
#3 * / // %
#4 + -

#5+3*2==11
#3*5+4**2==31
#3*(5+4)**2==243

#atividade

print(5+2*3)
print(5**2)
print(5**3)
print(19//2)
print(19/2)
print(365**522)
print(18%2)
print(122%3)
print('oi' + 'Olá')
print('oi' * 450)
print('=' * 20)

nome = input('Qual é seu nome?')
print('Prazer em te conhecer {:^20}!' .format(nome))

n1 = int(input('um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma vale {}, o produto {} e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e)) 