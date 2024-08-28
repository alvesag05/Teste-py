#exercicio 03
n1=int(input('digite um numero: '))
n2=int(input('digite outro numero: '))
s=n1+n2
print('O Valor da Soma foi: ',s)

#4
a = input('digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('só tem espaços? ', a.isspace())
print('é um numero? ', a.isnumeric())
print('é alfabetico? ', a.isalpha())
print('é alfanumerico? ', a.isalnum())