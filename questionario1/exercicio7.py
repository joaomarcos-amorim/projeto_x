#Escreva um programa que leia uma palavra e um número inteiro k e 
# identifique a k-ésima letra da palavra informada pelo usuário.

palavra = str(input('digite uma palavra:'))
quantidade= len(palavra)
k= int(input (f'digite a posição da letra desejada que não passe de {quantidade}:'))

print (f'a {k}ª letra da palavra é: {palavra[k-1]}')

