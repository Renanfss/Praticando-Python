import os

def funcao():
    horas = int(input('Digite o horario atual (o-23): '))

    if horas >= 8 and horas <= 18:
        print('Horario permitido entrada')
    else:
        print('Acesso negado.')
    
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