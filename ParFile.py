#!/usr/bin/env python
# -*- encondig: utf-8 *-*

class ParFile(object):
	"""docstring for ClassName"""

	def process(self, fileName):
		file = open(fileName, 'r')
		lines = file.readlines()
		par = ParImpar()
		par.jogador1 = lines[0]
		par.jogador2 = lines[1]
		numeroPartidas = int(lines[2])
		partidas = []
		for line in lines[3:numeroPartidas+3]:
			partida = Partida()
			partida.jogador1Jogada =int(line[0:1])
			partida.jogador2Jogada =int(line[2:3])
			partidas.append(partida)
		par.partidas = partidas
		self.processaVencedor(par)
		return par
	
	def processaVencedor(self,par):
		vencidasJogador1 = 0
		vencidasJogador2 = 0
		for partida in par.partidas:
			divisao = (partida.jogador1Jogada + partida.jogador2Jogada) % 2
			if divisao is 0:
				vencidasJogador1 = vencidasJogador1+1
			else:
				vencidasJogador2 = vencidasJogador2+1
		if vencidasJogador1 > vencidasJogador2:
			par.ganhador = par.jogador1
			return
		if vencidasJogador1 < vencidasJogador2:
			par.ganhador = par.jogador2
			return
		par.ganhador = 'Empate'
		pass


class ParImpar(object):
    jogador1 = None
    jogador2 = None
    ganhador = None
    partidas = []

class Partida(object):
	jogador1Jogada = None
	jogador2Jogada = None 