#Escreva um programa que leia os valores de dois ângulos 
# internos de um triângulo e calcule o valor do terceiro ângulo.

primeiro_angulo= int(input( 'digite o valor do primeiro angulo'))
segundo_angulo= int(input( 'digite o valor do segundo angulo'))
terceiro_angulo = ( 180 - (primeiro_angulo + segundo_angulo) )

print ( f'o valor do terceiro angulo é de: {terceiro_angulo}°' )