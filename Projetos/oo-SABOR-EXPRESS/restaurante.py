class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False #Ao colocar _ na frente do atributo, estamos indicando que ele é privado
        Restaurante.restaurantes.append(self) 
        
    def __str__(self):     # O metodo __str__ é chamado quando usamos print() no objeto
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiano")

Restaurante.listar_restaurantes()