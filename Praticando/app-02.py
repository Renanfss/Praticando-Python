def proximo(texto):
    import os
    print(f'Proximo exercicio: {texto}')
    input('Pressione qualquer tecla para continuar...')
    os.system('cls')


# 1. Dicionario

pessoa = {'nome':'Lucas', 'idade':19, 'cidade':'São Paulo'}

proximo('Modificar valor')

# 1.1 Modificar valor
nova_idade = int(input('Digite a nova idade: '))
pessoa['idade'] = nova_idade

profissao = input(f'Digite a profissão de {pessoa['nome']}: ')
pessoa['profissao'] = profissao

item_remover = input(print(f'Qual item você deseja remover?'))
pessoa.pop(item_remover)
print(pessoa)

proximo('Relação de números e seu quadrado')

# 2 Relação de números e seu quadrado 
numeros_quadrados = {x: x**2 for x in range(1, 6)} 
print(numeros_quadrados)

proximo('Verificar existencia de chave')

# 3. Verificar existencia de chave
chave = input('Digite a chave que deseja verificar: ')
if chave in pessoa:
    print(f'A chave {chave} existe no dicionario')
else:
    print(f'A chave {chave} não existe no dicionario')

proximo('Contar palavras em uma frase')

# 4. Contar palavras em uma frase
frase = "learning nuvem análise tecnologia dados análise big sistemas ciência inteligência tecnologia internet big computador artificial artificial artificial sistemas ciência tecnologia"
palavras = frase.split()
contagem_palavras = {}

for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)



