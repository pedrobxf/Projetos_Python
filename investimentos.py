inicial = float(input('Digite o valor inicial: '))
aporte = float(input('Digite o valor do aporte mensal: '))
juros = float(input('Digite o valor dos juros mensais: '))
tempo = int(input('Digite o tempo em meses: '))

total = inicial
for i in range(tempo):
    total += aporte
    total += total * (juros / 100)

print(f'O valor total é de R$ {total:.2f}')
