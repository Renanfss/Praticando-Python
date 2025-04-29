def proximo(texto):
    import os
    print(f'Proximo exercicio: {texto}')
    input('Pressione qualquer tecla para continuar...')
    os.system('cls')

# 1. listas
numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Lucas', 'João', 'Maria', 'Ana', 'Pedro']
ano = [2004, 2025]

proximo('Loops')

# 2. Loops
for numero in numeros:
    print(numero)
else: 
    print('Todos os números foram exibidos!')

proximo('Soma dos números ímpares')

# 2.1 Soma dos números ímpares
n1 = 0
for numero in numeros:
    if numero % 2 == 1:
        n1 += numero
else:
    print(f'A soma dos números ímpares é: {n1}')

proximo('Inverter lista')

# 2.2 Inverter lista
lista_invertida = numeros[::-1] 
#O fateamento indica que queremos percorrer a lista, mas com o passo negativo, resultando na inversão da lista
print(f'A lista invertida é {lista_invertida}')

proximo('Tabuada')

# 2.3 Tabuada
n1 = int(input('Digite um número para ver a tabuada: '))
for i in range(1, 10):
    print(f'{n1} x {i} = {n1*i}')

proximo('Soma de lista')

# 2.4 Soma de lista
try:
    n1 = 0
    for numero in numeros:
        n1 += numero
    else:
        print(f'A soma dos números é: {n1}')  
except:
    print('Erro! Não foi possível somar os números!')

proximo('Média')

# 3. Média 
valores = input('Digite os valores separados por espaço: ').split()
valores_convertidos = []
for valor in valores:
    valores_convertidos.append(float(valor))

try:
    media = sum(valores_convertidos) / len(valores_convertidos)
    print(f'A média dos valores é: {media:.2f}') 
except ZeroDivisionError:
    print('Erro: a lista está vazia! Não é possível calcular a média.')
except ValueError:
    print('Erro: você digitou algo que não é número!')
except Exception as e:
    print(f'Erro inesperado: {e}')
