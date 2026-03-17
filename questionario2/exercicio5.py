#Escreva um programa que leia a idade de uma pessoa e verifique se ela é criança (0-12 anos), 
#adolescente (13-17 anos), adulta (18-59) ou idosa (acima de 60 anos).

idade_pessoa = int(input('Digite a sua idade:'))

if (0<= idade_pessoa <= 12):
    print("é uma criança")

elif(13<= idade_pessoa <=17):
    print('é um adolescente')

elif(18 <= idade_pessoa <= 59):
    print('é um adulto')

else:
    print(' é um idoso')
