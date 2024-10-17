import random 
import string

tamanho = int(input('Digite o tamanho da senha: '))

incluir_maisculas = input('Incluir letras maiúsculas? [s/n]: ').lower() == 's'
incluir_minusculas = input('Incluir letras minúsculas? [s/n]: ').lower() == 's'
incluir_numeros = input('Incluir números? [s/n]: ').lower() == 's'
incluir_simbolos = input('Incluir caracteres especiais? [s/n]: ').lower() == 's'

caracteres = ''

if incluir_maisculas:
    caracteres += string.ascii_uppercase
if incluir_minusculas:
    caracteres += string.ascii_lowercase
if incluir_numeros:
    caracteres += string.digits
if incluir_simbolos:
    caracteres += string.punctuation

senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

print(f'Senha gerada: {senha}')