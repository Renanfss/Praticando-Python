'''
Uma escola está organizando os dados dos alunos para criar um relatório resumido. Cada aluno tem seus dados registrados em uma única entrada, incluindo nome, idade e nota final no semestre. Esses dados devem ser exibidos separadamente para cada aluno no formato abaixo:

Aluno: Nome
Idade: Idade
Nota: Nota
Copiar código
Ajude a escola a desenvolver um programa que registre as informações dos alunos, organize os dados e exiba um relatório detalhado com as informações separadamente.

Exemplo de Entrada:

Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: João, 16, 8.5, Maria, 17, 9.2, Pedro, 15, 7.8
Copiar código
Saída esperada:

Aluno: João
Idade: 16
Nota: 8.5

Aluno: Maria
Idade: 17
Nota: 9.2

Aluno: Pedro
Idade: 15
Nota: 7.8
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