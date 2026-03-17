#Escreva um programa que leia três números e seus respectivos pesos e calcule a sua média ponderada

num1 = int(input( 'digite o primeiro numero'))
num2 = int(input( 'digite o segundo numero'))
num3 = int(input( 'digite o terceiro numero'))

peso1 = int(input( 'digite o primeiro peso'))
peso2 = int(input( 'digite o segundo peso'))
peso3 = int(input( 'digite o terceiro peso'))

soma_pesos = (peso1 + peso2 + peso3)
media_ponderada = ((num1 * peso1) + (num2 * peso2) + (num3 * peso3)) / soma_pesos

print (f' a media ponderada dos numeros {num1}, {num2} e {num3}, com os respectivos pesos {peso1}, {peso2} e {peso3} é: {media_ponderada}')