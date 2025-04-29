import os
def verifica_vendas():
    banana = input('Digite a quantidade de bananas vendidas no mês: ')
    maca = input('Digite a quantidade de maçãs vendidas no mês: ')

    if banana > maca:
        os.system('cls')
        print('O vendedor vendeu mais bananas do que maçãs!')
    elif banana < maca:
        os.system('cls')
        print('O vendedor vendeu mais maçãs do que bananas!')
    else:
        os.system('cls')
        print('O vendedor vendeu a mesma quantidade de bananas e maçãs.')

def main():
    os.system('cls')
    verifica_vendas()
    opcao = input('\nClique 1 para voltar ao menu principal ou qualquer outra tecla para sair: ') 
    match opcao:
        case '1':
            main()
        case _:
            print('Programa finalizado')

if __name__ == '__main__':
    main()