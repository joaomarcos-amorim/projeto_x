#Escreva um programa que leia o valor de um ano e verifique se ele é ou não bissexto. Um ano é bissexto se ele for divisível
#por quatrocentos ou se se ele for divisível por 4, mas não for divisível por 100.

ano = int(input ('digite o ano'))

if (ano % 400 == 0 or ano % 4 == 0):
    print(' É um ano bissexto')

else:
    print('Não é Bisexto')
    