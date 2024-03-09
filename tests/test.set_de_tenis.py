import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.set_de_tenis import evaluar

class TestSetDeTenis(unittest.TestCase):
    def test_aun_no_termina(self):
        valor_esperado = "Aún no termina"
        valor_actual = evaluar(4, 5)
        self.assertEqual(valor_esperado, valor_actual)

class TestSetDeTenis(unittest.TestCase):
    def test_terminado_A(self):
        valor_esperado = "El ganador es A"
        valor_actual = evaluar(6, 4)
        self.assertEqual(valor_esperado, valor_actual)        

class TestSetDeTenis(unittest.TestCase):
    def test_terminado_B(self):
        valor_esperado = "El ganador es B"
        valor_actual = evaluar(4, 6)
        self.assertEqual(valor_esperado, valor_actual)

class TestSetDeTenis(unittest.TestCase):
    def test_valor_invalido(self):
        valor_esperado = "El resultado no es valido"
        valor_actual = evaluar(8, 6)
        self.assertEqual(valor_esperado, valor_actual)            

class TestSetDeTenis(unittest.TestCase):
    def test_valor_invalido(self):
        valor_esperado = "El resultado no es valido"
        valor_actual = evaluar(-1, 2)
        self.assertEqual(valor_esperado, valor_actual)
    

if __name__ == '__main__':
    unittest.main()
