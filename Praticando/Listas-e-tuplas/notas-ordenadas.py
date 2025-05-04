'''
    Resebe uma lista de notas, separadas por espaço, separa essa string de entrada e converte seus elementos para inteiros.
    Retorna a lista de notas ordenadas.
'''

entrada_notas = input('Digite todas as notas separadas por um espaço: ')
notas = [int(n) for n in entrada_notas.split()] #list comprehension
print(f'Notas: {sorted(notas)}') #O método sorted() retorna uma nova lista ordenada, sem alterar a lista original como o método sort() faria.


