#atividade005

#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor
#crie um algoritimo que leia um número e mostro seu dobro, triplo raiz quadrada
#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
#faça um programa que leia um número inteiro qualque e mostre na tela a sua tabuada
#crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidadde de tinta necessaria para pinta-la, sabenddo que cada litro de tinta, pinta uma área de 2m ao quadrados
#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
#Faça um algoritmo que leia o salário,com 15% de aumento

#1
n1 = int(input('Escreva um Numero: '))
s = n1 + 1
x = n1 - 1
print('O sucessor de {}, o antecessor é {}'.format(s,x), end=' ')

#2

n2 = int(input('Digite um número: '))
m = n2 * 2
d = n2 * 3
r = n2 ** (1/2)
print('O dobro de {}, o triplo de {} e a raiz de {}'.format(m,d,r), end =' ')

#3

n3 = int(input('Digite a nota um do Aluno: '))
n4 = int(input('Digite a nota dois do Aluno: '))
e = n3 + n4 // 2 
print('Resultado da nota é {}'.format(e), end=' ')

#4

medida=float(input('uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('a media de {}m corresponde a {}cm e {}mm'.format(medida,cm, mm))