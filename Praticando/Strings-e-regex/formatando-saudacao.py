"""
Gera uma mensagem de boas-vindas personalizada com base no nome e na cidade do cliente.  
"""
entrada = input('Olá, informe o nome e cidade do cliente separados por um espaço: ')
info = entrada.strip().split()

print(f'Olá, {info[0].title()}! Bem-vinda ao sistema da cidade de {info[1].title()} teste')
