import unittest

from src.lotomania.lotomania import Lotomania

class TestLotomania(unittest.TestCase):

    jogo = []

    def setUp(self) -> None:
        self.jogo = Lotomania()
        return super().setUp()

    def test_escolher_numero_entre_1_e_99(self):
        self.jogo.addNumero()
        self.assertCountEqual(self.jogo.length(), 1);
