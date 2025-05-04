'''
Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.

Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?

Exemplo de Entrada:

Produtos do estoque 1 (separados por vírgula): Arroz, Feijão, Macarrão
Produtos do estoque 2 (separados por vírgula): Óleo, Sal, Açúcar
Copiar código
Saída esperada:

Estoque combinado:
('Arroz', 'Feijão', 'Macarrão', 'Óleo', 'Sal', 'Açúcar')
'''

estoque1 = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(","))
estoque2 = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(","))
juntura = estoque1 + estoque2 
nova_tupla = tuple(elemento.strip() for elemento in juntura)  # Remove espaços em branco
    
print(f"Estoque combinado: {nova_tupla}")




