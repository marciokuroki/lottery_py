import random
from typing import Final
class Lotofacil:
    LIMITE_SUPERIOR: Final[int] = 25
    LIMITE_INFERIOR: Final[int] = 1
    jogo = []
    qtd_dezenas = 0

    def __init__(self, jogo) -> None:
        self.jogo = jogo

    def quantidade_dezenas(self, qtd):
        self.quantidade_dezenas = qtd

    def add_numero(self):
        global LIMITE_SUPERIOR, LIMITE_INFERIOR
        numero_escolhido = random.randint(LIMITE_INFERIOR, LIMITE_SUPERIOR)
        if (numero_escolhido not in self.jogo): 
            if (self.jogo.length() < self.qtd_dezenas):
                self.jogo.append()