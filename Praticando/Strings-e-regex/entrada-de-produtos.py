"""
Padroniza o nome de um produto convertendo todas as letras para minúsculas  
e removendo espaços desnecessários no início e no final.
"""
produto = input('Escreva o nome do produto: ')
print(f'Nome do produto é: {produto.strip().lower()}')