from random import randint

while True:
    print('Lançando os dados...')
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    soma = dado1 + dado2
    print(f'Dado 1: {dado1}')
    print(f'Dado 2: {dado2}')
    print(f'Soma: {soma}')

    while True:
        opcao = input('Você quer lançar os dados novamente? [S/N]: ').upper().strip()
        if opcao == 'S':  
            break
        elif opcao == 'N':  
            print('<< Encerrando o programa >>')
            exit() 
        else:
            print("Opção inválida. Digite 'S' para continuar ou 'N' para sair.")
