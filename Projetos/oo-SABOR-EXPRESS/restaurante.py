class Restaurante:
    restaurantes = [] #atributo da classe, que armazena todos os restaurantes criados

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False #Ao colocar _ na frente do atributo, estamos indicando que ele é privado
        Restaurante.restaurantes.append(self) 
        
    def __str__(self):     # O metodo __str__ é chamado quando usamos print() no objeto
       return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.ativo}')
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_praca.alterar_estado()
restaurante_pizza = Restaurante("Pizza Express", "Italiano")

Restaurante.listar_restaurantes()

print(f'{Restaurante.restaurantes[1]}')