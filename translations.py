# -*- coding: utf-8 -*-
from os import listdir

#variáveis para listar arquivos
scripts = []
csvs = []

#listando os scripts e os CSVs, criar as pastas depois.
for f in listdir("scripts"):
	scripts.append(str(f))

for f in listdir("csvs"):
	csvs.append(str(f))

cData = open("csvs/"+csvs[0], encoding="latin-1").readlines()
#alteração para sempre pegar o csv na posição zero, para que se use apenas 1 csv. 

idxScrpt = 1
#variável a ser usada quando tiver sendo usado apenas um csv

idx = 0
for script in scripts:
	saida = open("saida/"+script, "w")
	#criação do arquivo de ´saída com o mesmo nome do arquivo de script

	sData = open("scripts/"+script, encoding="latin-1").readlines()
	#cData = open("csvs/"+csvs[idx], encoding="latin-1").readlines()
	#o for itera todos os arquivos na pasta script, e então abro ele separando por linha, então faço o mesmo com o CSV na mesma posição

	#idxScrpt = 1
	for linha in sData:
		linha = linha.split('"')

		if len(linha) == 1:
			saida.write(linha[0])
		else:
			trslt = cData[idxScrpt].split(';')
			saida.write(linha[0]+'"'+trslt[1]+'"\n')
			idxScrpt += 1

	saida.close()
	idx += 1
