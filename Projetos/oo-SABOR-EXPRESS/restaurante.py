class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante() #Criação do objeto
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print()
