import math

numero = float(input('Digite um número: '))

raiz_quadrada = math.sqrt(numero)
print(f'A raiz quadrada de {int(numero)} é {raiz_quadrada}')

seno = math.sin(numero)
print(f'O seno de {int(numero)} (em radianos) é {seno}')

if numero.is_integer() and numero >= 0:
    fatorial = math.factorial(int(numero))
    print(f'O fatorial de {int(numero)} é {fatorial}')
else:
    print('Fatorial só pode ser calculado para números inteiros positivos.')