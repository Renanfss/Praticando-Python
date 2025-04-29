import os

def funcao():
    notas = []

    for i in range(1,4):
        nota = float(input(f'Digite a nota {i}: '))
        notas.append(nota)
    soma = sum(notas)
    media = soma / len(notas)
    os.system('cls')
    print(f'A media final do Aluno é de {media:.2f}')

    if media >=7:
        print('Aluno aprovado!')
    elif media >= 5:
        print('Aluno em recuperação!')
    else:
        print('Aluno reprovado!')
    
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