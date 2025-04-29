estoque = int(input('Informe a quantidade de livros disponiveis: '))

while estoque != 0:
    opcao = input('Digite 1 caso tenha realizado uma venda: ')
    match opcao:
            case '1':
                estoque -=  1
                print(f'Venda realizada! Estoque restante: {estoque}')
            case _:
                continue

