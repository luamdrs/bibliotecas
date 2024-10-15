from datetime import datetime

data_futura = input('Digite uma data futura (dd/mm/aaaa): ')

futura = datetime.strptime(data_futura, '%d/%m/%Y')

data_atual = datetime.today()

diferenca = futura - data_atual

faltam_dias = diferenca.days

print(f'Faltam {faltam_dias} dias para a data {data_futura}.')