#Escreva um programa que leia a quantidade de horas trabalhadas por um funcionário de uma empresa 
# durante um mês e o valor de cada hora trabalhada e determine o seu pagamento. O programa deve 
# considerar que a carga-horária mensal do funcionário é de 160 horas e que o valor de cada hora extra 
# corresponde ao valor da hora trabalhada acrescido de uma taxa de 50%. Para resolver a questão, 
# considere que a quantidade de horas trabalhadas nunca será inferior a 160

horas_trabalhadas = float(input('digite quais foram suas horas trabalhadas:'))
valor_por_hora = float(input ('digite o valor em R$ por hora'))
horas_minimas = 160
horas_extras = horas_trabalhadas - horas_minimas
salario_base = horas_minimas * valor_por_hora
valor_horas_extras = (1.50 * (valor_por_hora * horas_extras))
salario_total = (salario_base + valor_horas_extras)
print (f'seu salario total é de: R${salario_total:.2f}')