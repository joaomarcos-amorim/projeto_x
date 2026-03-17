#Escreva um programa que leia o valor de uma passagem em reais e em milhas e, em seguida, leia o valor 
# da passagem (em reais) que Caio deseja comprar e calcule quantas milhas ele precisa juntar 
# para que ele não precise pagar pela passagem. Para resolver este programa, 
# considere que a proporção entre o valor da milha e o valor em reais é o mesmo para todos os 
# voos da companhia aérea.

valor_passagem_milhas = float(input('Digite o valor da passagem em milhas:'))
valor_passagem_reais = float(input('Digite o valor da passagem em R$:'))
valor_milha_por_real = valor_passagem_milhas / valor_passagem_reais

passagem_desejada = float(input('Digite o valor da passagem desejada em R$:'))
milhas_passagem_desejada = valor_milha_por_real * passagem_desejada

print(f'Caio precisa juntar {milhas_passagem_desejada} milhas para pagar a passagem')

