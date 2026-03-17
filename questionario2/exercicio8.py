#Escreva um programa que leia os valores dos três lados de um triângulo e o classifique como equilátero, isósceles ou
#escaleno

primeiro_lado = int(input('Digite o primeiro lado do triangulo'))
segundo_lado = int(input('Digite o segundo lado do triangulo'))
terceiro_lado = int(input('Digite o terceiro lado do triangulo'))

if ( primeiro_lado == segundo_lado == terceiro_lado):
    print('É um triangulo equilátero')

elif( primeiro_lado == segundo_lado != terceiro_lado or primeiro_lado != segundo_lado == terceiro_lado):
    print('É um triangulo isósceles')