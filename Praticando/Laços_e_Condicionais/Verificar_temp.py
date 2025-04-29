import os

def funcao():
    temp = int(input('Digite a temperatura em graus Celsius atual: '))

    if temp > 25:
        print('Alerta! A temperatura está acima do limite permitido de 25 graus Celsius.')
    else:
        print('A temperatura está dentro do limite permitido.')

def main():
    os.system('cls')
    funcao()
    opcao = input('\nClique 1 para voltar ao menu principal ou qualquer outra tecla para sair: ') 
    match opcao:
        case '1':
            main()
        case _:
            os.system('cls')
            print('Programa finalizado')

if __name__ == '__main__':
    main()