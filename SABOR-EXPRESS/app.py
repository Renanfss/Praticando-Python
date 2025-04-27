import os

restaurantes = ['Pizza', 'Lasanha', 'Macarrão']




def exibir_nome_e_opcoes():
    print('Sabor Express\n')

    print('1. Cadastrar restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('3. Ativar Restaurante')
            case 4: 
                print('Programa finalizado!')
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()

def cadastrar_novo_restaurante():
    exibir_subtitulo ('--Cadastro de novos restaurantes--')
    nome_do_restaurente = input('Digite o nome do restaurante que deseja dastar: ')
    restaurantes.append(nome_do_restaurente)
    print(f'O restaurante {nome_do_restaurente} foi castrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo ('Listando restaurantes')
    
    for restaurante in restaurantes:
        print(f'. {restaurante}')

    voltar_menu()

def finalizar_app():
    exibir_subtitulo ('Programa finalizado')

def exibir_subtitulo (texto):
    os.system('cls')
    print(f'{texto}\n')



def voltar_menu ():
    input('\nClique em qualquer tecla para voltar ao menu principal') 
    main()

def opcao_invalida():
    print('Opção invalida!\n')
    voltar_menu ()

def main():
    os.system('cls')
    exibir_nome_e_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()

 