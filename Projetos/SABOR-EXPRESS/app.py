import os

# lista de dicionários com os restaurantes cadastrados
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_e_opcoes(): 
    '''Função que exibe o nome do programa e as opções disponíveis no menu principal'''

    print('Sabor Express\n')

    print('1. Cadastrar restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def escolher_opcao():
    ''''Fução recebe a opção escolhida pelo usuário e executa a função correspondente'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_estado_restaurante()
            case 4: 
                print('Programa finalizado!')
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()

def cadastrar_novo_restaurante():
    '''' Função que cadastra um novo restaurante na lista de restaurantes
     inputs: nome e categoria do restaurante
     outputs: dicionario com os dados do restaurante e adiciona a lista de restaurantes
    '''
    exibir_subtitulo ('--Cadastro de novos restaurantes--')
    nome_do_restaurente = input('Digite o nome do restaurante que deseja cadastar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurente}: ')
    dados_do_restaurante = {'nome': nome_do_restaurente, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurente} foi castrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    '''''Função que lista os restaurantes cadastrados na lista de restaurantes
    outputs: imprime os dados de cada restaurante na tela'''
    exibir_subtitulo ('Listando restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(23)} | Status\n')
    #A função ljust() alinha o texto a esquerda, e o valor dentro dos parenteses é o tamanho da string
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = "Ativo" if restaurante['ativo'] else "Inativo" 
        print(f' - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')

    voltar_menu()

def alterar_estado_restaurante():
    ''''Função que altera o estado do restaurante (ativo/inativo)
    inputs: nome do restaurante
    outputs: altera o valor do campo ativo no dicionario do restaurante e imprime na tela o novo status
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    nome_encontrado = False

    for restaurante in restaurantes: 
        if restaurante['nome'] == nome_restaurante:
            nome_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] #not inverte o valor booleano
            print(f'O restaurante {nome_restaurante} foi {"ativado" if restaurante["ativo"] else "desativado"} com sucesso!') #operador ternario para verificar se o restaurente foi ativado ou desativado
    if nome_encontrado == False:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
    voltar_menu()

def finalizar_app():
    exibir_subtitulo ('Programa finalizado')

def exibir_subtitulo (texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha) 



def voltar_menu ():
    input('\nClique em qualquer tecla para voltar ao menu principal') 
    main()

def opcao_invalida():
    print('Opção invalida!\n')
    voltar_menu ()

def main():
    '''''Função principal que executa o programa'''
    os.system('cls')
    exibir_nome_e_opcoes()
    escolher_opcao()

if __name__ == '__main__': #Executa a função main se o arquivo for executado diretamente
    main()

 