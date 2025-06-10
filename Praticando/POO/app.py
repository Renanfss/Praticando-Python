class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome.ljust(20)} | {self.idade.ljust(20)} | {self.idade.ljust(20)}'
    
    def aniversario(self):
        self.idade += 1

    def saudacao(self):
        if self.profissao:
            print(f'Olá sou {self.nome}! Trabalho como {self.profissao}')
        else:
            print(f'Olá sou {self.nome}')
    
