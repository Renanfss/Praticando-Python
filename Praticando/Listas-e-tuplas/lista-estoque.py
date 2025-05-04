'''
    Verifica se um determinado item está disponivel em uma lista
    Retorna se está disponivel ou precisa ser comprado
'''

despensa = ['banana', 'maça', 'açucar', 'leite', 'arroz', 'feijão', 'sal', 'farinha', 'óleo', 'macarrão']
item = input('Digite o item que você quer verificar: ')

if item in despensa:
    print(f'O item {item} está disponivel.')
else:
    print(f'O item {item} precisa ser comprado')