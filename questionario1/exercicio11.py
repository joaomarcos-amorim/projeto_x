#Um banco está realizando uma grande promoção em seus financiamentos. Ele financia qualquer 
# valor em 5 prestações. O valor da primeira prestação corresponde à 20% do valor do empréstimo. 
# Os valores das demais prestações correspondem ao valor da parcela anterior acrescido de uma taxa 
# de juros de 7%. Com base nestas informações, escreva um programa que leia o valor a ser financiado 
# por um cliente e calcule: o valor de cada prestação, o valor total 
# que o cliente vai pagar pelo empréstimo e o total de 
# juros que o cliente vai pagar pelo empréstimo

valor_financiado = float (input('digite o valor financiado:'))
primeira_prest = 0.20 * valor_financiado
segunda_prest = primeira_prest * 1.07
terceira_prest = segunda_prest * 1.07
quarta_prest = terceira_prest * 1.07
quinta_prest = quarta_prest * 1.07
valor_total_das_prest = primeira_prest + segunda_prest + terceira_prest + quarta_prest + quinta_prest
valor_juros = valor_total_das_prest - valor_financiado

print(f'o valor da primeira a quinta parcela é respectivamente de:R$\
{primeira_prest:.2f}, R${segunda_prest:.2f}, R${terceira_prest:.2f}, R${quarta_prest:.2f}, R${quinta_prest:.2f}.')

print(f'O valor total a ser pago é:R${valor_total_das_prest:.2f}, e o valor do juros é de:R$ {valor_juros:.2f}')