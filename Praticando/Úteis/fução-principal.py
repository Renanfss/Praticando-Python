'''
    Essa função é um exemplo de como criar uma função principal em Python, útil para organizar e facilitar o teste dos scripts.
    Ela chama a função funcao() que executa um código específico, e depois pergunta ao usuário se deseja voltar ao menu principal ou sair do programa.
'''

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