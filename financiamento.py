imovel = float(input('Digite o valor do imóvel: '))
entrada = float(input('Digite o valor da entrada: '))
tempo = int(input('Digite o número de parcelas: '))
taxa = float(input('Digite o valor dos juros mensais: '))
tipo = input('Digite o tipo de financiamento (S para SAC, P para PRICE): ')

if tipo == 'S':
    saldo = imovel - entrada
    amortizacao = saldo/ tempo
    for mes in range(1,tempo+1):
        juros = saldo*(taxa / 100)
        parcela = amortizacao + juros
        saldo -= amortizacao
        print(f'Parcela {mes}: R$ {parcela:.2f}') 

elif tipo == 'P':
    saldo = imovel - entrada
    parcela = (saldo* (taxa/100)) / (1 - (1 + (taxa/100)) ** -tempo)
    print(f'\nValor da parcela fixa: R$ {parcela:.2f}')
