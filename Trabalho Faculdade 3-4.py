# Começo da função volumeFeijoada
def volumeFeijoada():
    global conta_volume

    print('Menu Volume Feijoada')

    try:
        volume = int(input("Entre com a quantidade que deseja (ml): "))

    except ValueError:
        print('Pare de digitar valores não númericos. Tente novamente!')
        return volumeFeijoada()

    else:
        if (volume >= 300) and (volume <= 5000):
            conta_volume = volume * 0.08

        else:
            print('Não aceitamos porções menores que 300ml ou maiores que 5l. Tente novamente!')
            return volumeFeijoada()
# Fim da função volumeFeijoada

# Começo da função opcaoFeijoada
def opcaoFeijoada():
    global conta_opcao
    opcoes = input('\nMenu Opção Feijoada'
                   '\nb - Básica (Feijão + Paiol + Costelinha)'
                   '\np - Premium (Feijão + Paiol + Costelinha + Partes de Porco)'
                   '\ns - Suprema (Feijão + Paiol + Costelinha + Partes de Porco + Charque + Calabresa + Bacon)\n'
                   'Entre com a opção da feijoada: ')

    if (opcoes == 'b'):
        conta_opcao = 1.00

    elif (opcoes == 'p'):
        conta_opcao = 1.25

    elif (opcoes == 's'):
        conta_opcao = 1.50

    else:
        print('Digitie uma opção válida!')
        return opcaoFeijoada()
# fim da função opcaoFeijoada

# Começo da função acompanhamentoFeijoada
def acompanhamentoFeijoada():
    global conta_adicional

    conta_adicional = 0

    while True:
        adicional = input('\nMenu Opção Acompanhamento Feijoada'
                          '\n0- Não desejo mais acompanhamentos'
                          '\n1- 200g de arroz '
                          '\n2- 150g de farofa '
                          '\n3- 100g de couve cozida '
                          '\n4- 1 laranja descascada '
                          '\nDeseja mais algum acompanhamento: ')

        if (adicional == '1'):
             conta_adicional += 5.00

        elif (adicional == '2'):
             conta_adicional += 6.00

        elif (adicional == '3'):
             conta_adicional += 7.00

        elif (adicional == '4'):
            conta_adicional += 3.00

        elif (adicional == '0'):
            print('Seu pedido está sendo encerrado...')

            break

        else:
            print('Digitie uma opção válida!')
# Fim da função acompanhamentoFeijoada

# Progama principal
print('Bem-vindo ao Progama de Feijoda do Luiz Fernando Valentim (RU: 4173542)')

volumeFeijoada()
opcaoFeijoada()
acompanhamentoFeijoada()

total = (conta_volume * conta_opcao) + conta_adicional

print('O valor a ser pago é R$: {:.2f}'.format(total))



            
