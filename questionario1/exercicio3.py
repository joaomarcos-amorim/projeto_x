#Escreva um programa que leia um número inteiro e informe o seu antecessor e o seu sucessor.

numero = int(input ( 'digite o numero inteiro:'))
numero_antecessor = (numero - 1)
numero_sucessor = (numero + 1)

print(f' o antecessor de {numero} é {numero_antecessor}, e o sucessor é {numero_sucessor}')