#Uma revendedora de veículos resolveu fazer uma promoção em seus veículos. Nesta revendedora, o preço de um
#veículo é calculado através do seu preço de compra, mais uma taxa de 20% de IPI, 17% de ICMS e uma margem de lucro
#de 20%. Nesta promoção, a revendedora resolveu tirar o valor do IPI. Com base nestas informações, escreva um
#programa que leia o preço atual de um veículo e calcule qual deve ser o seu preço na promoção.

preco_de_compra = float(input('digite o valor de compra bruto do carro'))
IPI = 0.20
ICMS = 0.17
LUCRO = 0.20
preco_total = preco_de_compra * (1 + (IPI + ICMS + LUCRO))
preco_com_desconto = preco_de_compra * (1 + (ICMS + LUCRO))

print (f'o valor total do veiculo é de: R${preco_total: .2f}, e o preço com o desconto é de: R${preco_com_desconto: .2f}')