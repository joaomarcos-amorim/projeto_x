#Escreva um programa que leia um valor em real, a cotação atual do dólar e calcule o valor 
# informado pelo usuário em dólares.

valor_em_real = float(input( ' digite o valor em real:'))
valor_em_dolar = float(input( ' digite a cotação atual do dólar:'))
valor_convertido= ( valor_em_dolar * valor_em_real)
print (f' o valor em dolar de {valor_em_real}R$ é de: {valor_convertido}$')