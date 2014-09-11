#!/usr/bin/env python
# -*- encondig: utf-8 *-*

import unittest
from ParFile import ParFile
from ParFile import ParImpar

class TestParFunctions(unittest.TestCase):

 def setUp(self):
  self.createFile("novo.txt")
 
 def test_doisEhPar(self):
  partida = ParFile().process("novo.txt")
  self.assertEqual( partida.jogador1, "Joao\n")
  self.assertEqual( partida.jogador2, "Maria\n")
  self.assertEqual( partida.ganhador, "Maria\n")
  pass

 def createFile(self , name):
  file = open(name, "w")
  file.write("Joao\n")
  file.write("Maria\n")
  file.write("3\n")
  file.write("1-2\n")
  file.write("2-3\n")
  file.write("2-2\n")
  file.close()

if __name__ == '__main__':
    unittest.main() 
    