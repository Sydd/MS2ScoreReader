import re

def ScoreInMap(file):
	
	totalScore = 0
	
	lastID = 0
	
	mapa = open(file,'r')

	x = 0	

	for line in mapa:
		if x == 1:
			x = 2

			a = re.split('=',line)
			
			averageScore = GetAverageScore(a[3])
			
		elif  x == 2:
			x = 0

			a = re.split('=',line)
			cantidad = int(GetNumbers(a[3]))
			totalScore = totalScore + cantidad * averageScore
			print (' Se va a spawnear puntaje por '  + str(cantidad * averageScore))
		elif re.match('<Behaviour name="ENEMIESSPAWNER">',line):
			print("se encontro un spawner. ")
			x = 1
			
		elif re.match('(<Parameter type=\"0\" name=\"SCORE\".+)',line):
			print("se encontro un enemigo sin prefab. ")
			e = re.split('=',line)
			totalScore = totalScore + int(GetNumbers(e[3]))
			
		elif re.match('IdPrefab=(-32|-82|-132|-129|-389|-463|-584|-593|-361|-740|-376)',line):
			a = re.sub('[^0-9]','',line)
			totalScore = totalScore + ScoreByIdVerbose(a)
	
	return totalScore

def GetAverageScore(spawners):
	a = re.split('-',spawners)
	average = 0
	for e in a:
		if e != a[0]:
			average = average + ScoreById(GetNumbers(e))
	return int(average / (len(a) - 1))
	
def GetNumbers(str):
        return re.sub('[^0-9]','',str)

def ScoreById(id):
	
	score = 0
	id = '-' + id
	
	if id == '-32':
		score = 100
	elif id == '-82':
		score = 100
	elif id == '-132':
		score = 140
	elif id == '-129':
		score = 120
	elif id == '-389' or id == '-463':
		score = 100
	elif id == '-584':
		score = 180
	elif id == '-593':
		score = 100
	elif id == '-740':
		score = 2500	
	elif id == '-361':
		score = 100
	elif id == '-376':
		score = 60
		
	if score == 0:
		print(' NO SE ENCONTRO EL ENEMIGO CON EL ID ' + id + 'e')
		
	return score

def ScoreByIdVerbose(id):
	
	score = 0
	
	id = '-' + id
	
	if id == '-32':
		print('Se sumo un enemyShooter - 100')
		score = 100
	elif id == '-82':
		print ('Se sumo una mina voladora - 60')
		score = 60
	elif id == '-132':
		print ('Se sumo un melee - 140')
		score = 140
	elif id == '-129':
		print('Se sumo un parachute - 120')
		score = 120
	elif id == '-389' or id == '-463':
		print('Se sumo un ChainSaw - 100')
		score = 100
	elif id == '-584':
		print('Se sumo un Shield - 180')
		score = 180
	elif id == '-593':
		print ('Se sumo un tanquesito - 100')
		score = 100
	elif id == '-740':
		print ('Se sumo un chopper - 2500')
		score = 2500	
	elif id == '-361':
		print ('Se sumo un selfie - 100')
		score = 100
	elif id == '-376':
		print ('Se sumo una cajita - 60')
		score = 60
		
	if score == 0:
		print(' NO SE ENCONTRO EL ENEMIGO CON EL ID ' + id + 'e')
		
	return score

def Test():
	score = ScoreInMap('E:\\BACKUP\\Python\\ContadorDeScore\\lvl0101.JpcMap')
	print('El score maximo del nivel es ' + str(score))

def Test2():
	score = ScoreInMap('E:\\BACKUP\\Python\\ContadorDeScore\\lvl0127.JpcMap')
	print('El score maximo del nivel es ' + str(score))

def ReadMap(map):
	path = "C:\\MetalSoldiers2\\_editorproject\\BILLKILLEM\\Mapas\\lvl01"
	if map < 10:
		mapa = path + '0' + str(map) + '.jpcmap'
	else:
		mapa = path + str(map) + '.jpcmap'
	return ScoreInMap(mapa)
        

def ReadAllMaps(cantidad):

	path = "C:\\MetalSoldiers2\\_editorproject\\BILLKILLEM\\Mapas\\lvl01"

	resultado = open("E:\\BACKUP\\Python\\ContadorDeScore\\resultado.csv", "w")

	mapasConScore = 'sep=,\n'
	
	for x in range(1,cantidad):

		if x < 10:
		
			mapa = path + '0' + str(x) + '.jpcmap'
		else:
			mapa = path + str(x) + '.jpcmap'
		
		score = ScoreInMap(mapa)
		
		mapasConScore += str(x) + ',' + str(score) + '\n'
		print(str(score) + ' puntaje en el mapa ' + str(cantidad))
	resultado.write(mapasConScore)
	resultado.close()
