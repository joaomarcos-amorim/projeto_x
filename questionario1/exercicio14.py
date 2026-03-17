#Lázaro está muito feliz por ter enfim conseguido construir a sua casa própria. Sabendo-se que a 
# construção durou 180 dias de trabalho, escreva um programa que leia o número de 
# pedreiros que trabalhavam na obra, o número de ajudantes e o valor da diária do pedreiro 
# e calcule o gasto de Lázaro com a mão de obra. Para resolver este programa,
#considere que todos os pedreiros e ajudantes trabalharam todos os dias da obra e 
# que o valor da diária de cada ajudante corresponde à metade do valor da diária do pedreiro

dias_de_trabalho = 180
quantidade_pedreiros = int(input('Digite a quantidade de pedreiros:'))
quantidade_ajudantes = int(input('Digite a quantidade de ajudantes:'))

diaria_pedreiro = float(input('Digite o valor da diária do pedreiro:'))
diaria_ajudante = diaria_pedreiro / 2

gasto_pedreiro = (quantidade_pedreiros * diaria_pedreiro) * dias_de_trabalho
gasto_ajudante = (quantidade_ajudantes * diaria_ajudante) * dias_de_trabalho
gasto_total = gasto_ajudante + gasto_pedreiro

print(f'O gasto de pedreiros foi R${gasto_pedreiro: .2f}, e o de ajudante foi R${gasto_ajudante: .2f}.')
print(f'O gasto total foi de R${gasto_total: .2f}')

