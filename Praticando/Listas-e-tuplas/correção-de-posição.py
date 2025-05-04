'''
    Corrige a posição de um nome em uma lista de posições
    Entrada: Nome incorreto e nome correto
    Saída: Lista atualizada com o nome correto em sua posição
'''
def corrige_posicao(nome_errado, nome_correto, lista):
    for nome in lista:
        try:
            if nome == nome_errado:
                indice = lista.index(nome) # O método index() retorna o índice do primeiro elemento encontrado na lista
                classificacao[indice] = nome_correto 
                print(f'O nome {nome_errado} foi substituido por {nome_correto}')
                print(f'Lista atualizada: {classificacao}')
                break
        except:
            print(f'O nome {nome_errado} não foi encontrado na lista.')


classificacao = ['João', 'Roberto', 'Pedro', 'Thiago', 'Ana']
print(f'Lista atual: {classificacao}')
nome_errado = (input('Digite o nome incorreto: ')).title().strip()
nome_correto = (input('Digite o nome correto: ')).title().strip()
corrige_posicao(nome_errado, nome_correto, classificacao) 


