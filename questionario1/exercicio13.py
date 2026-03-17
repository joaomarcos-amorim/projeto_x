#Um provedor de internet oferece um plano promocional para os seus clientes. Neste plano, 
# ele paga uma mensalidade de R$ 80,00 e pode acessar até 100 GB de dados. 
# Caso a quantidade de dados acessados seja superior a este limite, ele deve pagar uma taxa 
# adicional de R$ 5,00 por cada GB extra acessado. Com base nestas informações, escreva um
#programa que leia a quantidade de dados acessados pelo cliente durante um mês (em GB) 
# e calcule o valor da sua conta, considerando que esta quantidade nunca é inferior a 100 GB.

dados_acessados = float(input('Digite em GB quantos dados foram ultilizados:'))
plano_padrão = 100.00
dados_fora_do_plano = dados_acessados - plano_padrão
taxa_adicional = dados_fora_do_plano * 5.00
valor_total_plano = 80.00 + taxa_adicional

print(f'o valor total da conta é de: {valor_total_plano}')