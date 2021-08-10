# -*- coding: utf-8 -*-
from os import listdir

csvs = []

for f in listdir("comma"):
	csvs.append(str(f))

for csv in csvs:
	saida = open("csvs/"+csv, "w")
	#criação do arquivo de ´saída com o mesmo nome do arquivo de csv

	cData = open("comma/"+csv, encoding="UTF-8").readlines()

	for linha in cData:
		linha = linha.split(',', 1)

		saida.write(linha[0]+';'+linha[1])

	saida.close()
