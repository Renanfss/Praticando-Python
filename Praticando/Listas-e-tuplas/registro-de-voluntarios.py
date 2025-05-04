'''
    Recebe nomes de voluntarios, armazena em uma lista e imprime a lista ao final.
'''
import os

voluntarios = []

while True:
    voluntario = input('Digite o nome do voluntário ou "sair" para encerrar e mostrar a lista de voluntários: ')

    if voluntario.lower() == 'sair':
        os.system('cls')
        print(f'Voluntários registrados:{voluntarios}')
        break
    else:
        voluntarios.append(voluntario)
        os.system('cls')
        print(f'O voluntario {voluntario} foi registrado com sucesso!')

