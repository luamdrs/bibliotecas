from random import randint

computador = randint(1, 20)
while True:
    numero = int(input('Digite um número entre 1-20: '))
    if numero < computador:
        print('O Chute um número mais alto...')
    elif numero > computador:
        print('Chute um número menor...')
    elif numero == computador:
        print(f'Você acertou! O computador escolheu o número {computador} e você digitou o número {numero}.') 
        break