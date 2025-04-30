"""
Verifica se uma URL começa com 'https://' e termina com '.com'.  
Retorna se a URL é válida ou inválida com base nesses critérios.
"""
entrada = input('Digite a URL para validação: ')
url = entrada.strip()

if url.startswith('https://') and url.endswith('.com'):
    print('URL válida!')
else:
    print('URL invalida!')


