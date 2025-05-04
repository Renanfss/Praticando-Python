'''
    Remove o último pedido de uma lista de pedidos
'''
import os

def remover_ultimo_pedido(lista):
    
    os.system('cls')
    pedidos.pop()
    print(f'A lista atualizada de pedidos é: {pedidos}')

pedidos = ['sanduíche', 'suco', 'sobremesa']

print(f'Pedidos feitos: {pedidos}')
remover = input('Deseja remover o último pedido? (s/n): ').strip().lower()
if remover == 's':
    remover_ultimo_pedido(pedidos)
