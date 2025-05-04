'''
Esse programa solicita ao usuário que insira os dados de alunos (nome, idade e nota) separados por vírgula.
Em seguida, ele processa esses dados em uma lista e exibe um relatório formatado com as informações de cada aluno.
'''

import os

def funcao():
    dados = input('Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ').split(',')
    print(f'\nRelatório dos alunos:\n')
    for i in range(0, len(dados), 3):
        print(f'Aluno: {dados[i].split()}')
        print(f'Idade: {dados[i+1].split()}')
        print(f'Nota: {dados[i+2].split()}\n')

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