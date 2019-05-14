import re

def ScoreInMap(file):
	
	totalScore = 0
		
	mapa = open(file,'r')

	x = 0

	for line in mapa:
		if x == 1:
		
			x = 2

			a = re.split('=',line)
			
			averageScore = 1
			
			if len(a) > 2:
				averageScore = GetAverageScore(a[3])
			else:
				averageScore = GetAverageScore(a[1])
		elif  x == 2:
			x = 0
			cantidad = 0
			a = re.split('=',line)
			if re.match('(TIMEBETWEENENEMIES.+)|(</Behaviou.+)',line):
				cantidad = 5
			else:
				if len(a) > 2:
					cantidad = int(GetNumbers(a[3]))
				else:
					cantidad = int(GetNumbers(a[1]))
			totalScore = totalScore + cantidad * averageScore
			print (' Se va a spawnear puntaje por '  + str(cantidad * averageScore))
			
		elif re.match('(<Behaviour name="ENEMIESSPAWNER">)|(NombreBH=ENEMIESSP)',line):
			print("se encontro un spawner. ")
			x = 1
			
		elif re.match('(<Parameter type=\"0\" name=\"SCORE\".+)',line):
			print("se encontro un enemigo sin prefab. ")
			e = re.split('=',line)
			totalScore = totalScore + int(GetNumbers(e[3]))
			
		elif re.match('IdPrefab=(-32|-82|-132|-129|-389|-463|-584|-593|-361|-740|-376)',line):
			a = re.sub('[^0-9]','',line)
			totalScore = totalScore + ScoreByIdVerbose(a)
	mapa.close()	
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

def ReadScore(map):
	path = "C:\\MetalSoldiers2\\_editorproject\\BILLKILLEM\\Mapas\\lvl01"
	if map < 10:
		mapa = path + '0' + str(map) + '.jpcmap'
	else:
		mapa = path + str(map) + '.jpcmap'
	return ScoreInMap(mapa)
	
def ReadAllScores(cantidad):

	path = "C:\\MetalSoldiers2\\_editorproject\\BILLKILLEM\\Mapas\\lvl01"

	resultado = open("E:\\BACKUP\\Python\\ContadorDeScore\\resultado.csv", "w")

	mapasConScore = 'sep=,\n'
	
	for x in range(1,cantidad):
		print("LEYENDO MAPA " + str(x))
		if x < 10:
		
			mapa = path + '0' + str(x) + '.jpcmap'
		else:
			mapa = path + str(x) + '.jpcmap'
		
		score = ReadScore(mapa)

		mapasConScore += str(x) + ',' + str(score) + '\n'
		print(str(score) + ' puntaje en el mapa ' + str(cantidad))
	resultado.write(mapasConScore)
	resultado.close()

def AddScore(map,goldScore,silverScore):
	
	print("Cambiando mapa numero " + str(map))

	path = "C:\\MetalSoldiers2\\_editorproject\\BILLKILLEM\\Mapas\\lvl01"


	if map < 10:
		map = '0' + str(map) + '.JpcMap'
	else:
		map = str(map) + '.JpcMap'
	
	mapa = open (path + map,"r")

	resultado = open('E:\\BACKUP\\Python\\ContadorDeScore\\Mapas\\lvl01'+ map,'w')

	lvlText = ''
	
	for line in mapa:
			if re.match('<Parameter type="0" name="SCORETOMEDAL01" value=".+',line):
				print("Cambiando moneda de oro")
				lvlText += '<Parameter type="0" name="SCORETOMEDAL01" value="' +  goldScore + '"/>\n'

			elif re.match('<Parameter type="0" name="SCORETOMEDAL02" value=".+',line):
				print("Cambiando moneda de plata")
				lvlText += '<Parameter type="0" name="SCORETOMEDAL02" value="' + silverScore + '"/>\n'

			else:
					lvlText += line

	resultado.write(lvlText)
	mapa.close()
	resultado.close()
	

def AddScoreAllMaps():


	resultado = open("E:\\BACKUP\\Python\\ContadorDeScore\\resultado.csv", "r")

	for line in resultado:
		
		data = re.split(";",line)
		
		AddScore(int(data[0]),GetNumbers(data[2]),GetNumbers(data[3]))
	




def Test():
	score = ScoreInMap('E:\\BACKUP\\Python\\ContadorDeScore\\lvl0101.JpcMap')
	print('El score maximo del nivel es ' + str(score))

def Test2():
	score = ScoreInMap('E:\\BACKUP\\Python\\ContadorDeScore\\lvl0127.JpcMap')
	print('El score maximo del nivel es ' + str(score))

def TestMedals():
	AddScore(1,'100','500')
	
AddScoreAllMaps()