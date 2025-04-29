import os

def funcao():
    tempos = []

    for i in range(1,4):
        tempo = int(input('Digite o tempo do projeto em dias:'))
        tempos.append(int(tempo))
        if tempo < 0:
            print('ERRO: O tempo não pode ser negativo.')
            return
    soma = sum(tempos) 
    print(f'O tempo total para conclusão dos projetos é de {soma} dias.')

def main():
    os.system('cls')
    funcao()
    opcao = input('\nClique 1 para voltar ao menu principal ou qualquer outra tecla para sair: ') 
    match opcao:
        case '1':
            main()
        case _:
            print('Programa finalizado')

if __name__ == '__main__':
    main()