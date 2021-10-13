import unittest

from src.mega.mega import Mega

class TestMega(unittest.TestCase):

    jogo = []

    def setUp(self) -> None:
        self.jogo = Mega()
        return super().setUp()

    def test_escolher_numero_entre_1_e_60(self):
        self.jogo.addNumero()
        self.assertCountEqual(self.jogo.length(), 1);
