'''
  Atualiza uma lista, adicionando um novo convidado em uma posição específica.
'''
import os

convidados = ['Ana', 'Pedro', 'Carlos']

print(f'Lista atual de convidados: {convidados}')
novo_convidado = input('Digite o nome do novo convidado: ')
posicao = int(input('Digite a posição na qual deseja inserir o convidado: '))

convidados.insert((posicao - 1), novo_convidado) #O método insert(). Este método recebe dois argumentos: o índice onde o elemento deve ser inserido e o próprio elemento a ser inserido
os.system('cls')

print(f'Lista atualizada de convidados: {convidados}')

