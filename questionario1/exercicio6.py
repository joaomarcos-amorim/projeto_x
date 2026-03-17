#Escreva um programa que leia um valor em KB e calcule o 
# seu valor correspondente em bits, bytes, MB e GB.

valor_kb = float(input('digite o valor em KB:'))
valor_em_bits = (valor_kb *(1024*8))
valor_em_bytes = (valor_kb * 1024)
valor_em_mb = (valor_em_bytes /1024)
valor_em_gb = (valor_em_mb / 1024)

print (f' valor de {valor_kb}KB em bits é de :{valor_em_bits}')
print (f' valor de {valor_kb}KB em bytes {valor_em_bytes}')
print (f' valor de {valor_kb}KB em MB é de :{valor_em_mb}')
print (f' valor de {valor_kb}KB em GB é de :{valor_em_gb: .2f}')