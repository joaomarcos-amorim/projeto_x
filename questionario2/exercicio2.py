#Escreva um programa que leia dois números e determine se o segundo número é menor, igual ou maior que o primeiro

num1 = int(input('digite o primeiro numero'))
num2 = int(input('digite o segundo numero'))

if (num2 < num1):
    print(f'o numero {num2} é menor que o número {num1}')

elif (num2 > num1):
    print(f' o numero {num2} é maior que o número {num1}')

else:
    print (f" o numero {num2} é igual ao numero {num1}")
