import random
class Lotofacil:
    jogo = []
    qtd_dezenas = 0

    def __init__(self, jogo) -> None:
        self.jogo = jogo

    def quantidade_dezenas(self, qtd):
        self.quantidade_dezenas = qtd

    def add_numero(self):        
        numero_escolhido = random.randint(1, 25)        
        if (numero_escolhido not in self.jogo): 
            if (self.jogo.length() < self.qtd_dezenas):
                self.jogo.append()