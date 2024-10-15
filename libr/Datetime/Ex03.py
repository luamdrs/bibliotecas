from datetime import datetime

data1 = input('Digite a primeira data (dd/mm/aaaa): ')
data2 = input('Digite a segunda data (dd/mm/aaaa): ')

data1_dt = datetime.strptime(data1, '%d/%m/%Y')
data2_dt = datetime.strptime(data2, '%d/%m/%Y')

diferenca = abs(data2_dt - data1_dt)

dias_totais = diferenca.days

anos = dias_totais // 365
meses = (dias_totais % 365) // 30
dias = (dias_totais % 365) % 30

print(f'A diferença entre as datas é de {dias_totais} dias.')
print(f'Isso equivale a {anos} anos, {meses} meses e {dias} dias.')