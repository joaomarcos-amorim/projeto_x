#Escreva um programa que leia um número inteiro e verifique se ele é positivo, negativo ou neutro.

numero = int(input('Digite o número inteiro:'))

if (numero > 0):
    print('O número é positivo')

elif (numero == 0):
    print('O número é neutro')

else:
    print('O número é negativo')