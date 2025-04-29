import os

def funcao():
    n = int(input('Digite um número: '))
    
    if (n % 2) != 0:
        print(f'O número {n} não é par')
    else:
        print(f'O número {n} é par')

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