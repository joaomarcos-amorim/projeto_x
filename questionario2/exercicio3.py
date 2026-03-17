#Escreva um programa que leia o número de gols marcados pelo time da casa e o número de gols marcado pelo time visitante e verifique se 
#o jogo foi vencido pelo time da casa, pelo time visitante ou se terminou empatado

gols_casa = int(input('digite a quantidade de gols feito pelo time da casa:'))
gols_visitante = int(input('digite a quantidade de gols feito pelo time visitante:'))

if(gols_casa > gols_visitante):
    print('o time da casa é vencedor')

elif(gols_casa < gols_visitante):
    print('o time visitante é vencedor')

else:
    print('o jogo saiu empate')