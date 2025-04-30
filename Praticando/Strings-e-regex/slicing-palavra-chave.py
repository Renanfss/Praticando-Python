"""
Recebe uma palavra do usuário e extrai as três primeiras e as três últimas letras.  
Exibe essas partes como pistas para uso em jogos ou desafios.
"""
palavra = input('Digite a palavra-chave: ')

print(f'Primeiras: {palavra[:3]}')
print(f'Ultimas: {palavra[-3:]}')
