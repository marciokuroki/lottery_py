import unittest

from src.lotofacil.lotofacil import Lotofacil

class TestLotofacil(unittest.TestCase):

    jogo = []

    def setUp(self) -> None:
        self.jogo = Lotofacil()
        return super().setUp()

    def test_escolher_numero_entre_1_e_25(self):
        self.jogo.addNumero()
        self.assertCountEqual(self.jogo.length(), 1);
