#Escreva um programa que leia um número inteiro e verifique se ele é par ou ímpar.

num = int(input('Digite um numero inteiro'))
resto = num % 2 
if (resto == 0):
    print(f'o numero {num} é par')

else:
    print(f"o numero {num} é impar")
