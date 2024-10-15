from datetime import datetime

data_nascimento = input('Digite sua data de nascimento (dd/mm/aaaa): ')

nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')

data_atual = datetime.today()

diferenca = data_atual - nascimento

anos = diferenca.days // 365
meses = (diferenca.days % 365) // 30
dias = (diferenca.days % 365) % 30

print(f'Você tem {anos} anos, {meses} meses e {dias} dias.')