'''
A professora Helena quer facilitar sua rotina na hora de calcular a média das notas finais da turma. Ela sempre anota as notas dos alunos ao longo do semestre e, no final, precisa de um relatório para saber se a turma está indo bem.

Para isso, ajude a professora a criar um programa que receba as notas finais de todos os alunos e calcule a média da turma.

Exemplo de Entrada:

Digite as notas dos alunos separadas por vírgula: 8.5, 7.0, 9.2, 6.8

Saída esperada:

Média final da turma: 7.88

'''
import os

def funcao():
    entrada_notas = input('Digite as notas dos alunos separadas por vírgula: ').strip().split(',')
    notas = [float(nota) for nota in entrada_notas]
    media = sum(notas) / len(notas)
    print(f'Média final da turma: {media:.2f}')

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
