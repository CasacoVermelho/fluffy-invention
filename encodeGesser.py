from os import listdir

files = []

for f in listdir("comma"):
	files.append(str(f))

for file in files:
	with open('comma/'+file) as f:
		print(f)
