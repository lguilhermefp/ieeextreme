import random

def NormalDiceRoll():
	face = random.randint(1, 6)
	if (face == 1):
		face = 111
	if (face == 2):
		face = 222
	if (face == 3):
		face = 333
	if (face == 4):
		face = 444
	if (face == 5):
		face = 555
	if (face == 6):
		face = 666
	return face


def toggleViciado(viciado):
	if(viciado):
		return False
	else:
		return True
	

def pointsInGameWithRoundsCount(roundAmount):
	i=0
	rollsAmountA = [0, 0, 0, 0, 0, 0, 0]
	rollsAmountB = [0, 0, 0, 0, 0, 0, 0]
	totalPointsA = 0
	totalPointsB = 0
	quemTaViciado = random.randint(1,2)
	AViciado = False
	BViciado = False

	if(quemTaViciado == 1):
		AViciado = True
		BViciado = False
	if(quemTaViciado == 2):
		AViciado = False
		BViciado = True		

	while(i<int(roundAmount)):
		if(AViciado):
			rollA = random.randint(1, 6)
			rollB = NormalDiceRoll()

			if(rollB == 111):
				rollsAmountB[1] += rollB
			if(rollB == 222):
				rollsAmountB[2] += rollB
			if(rollB == 333):
				rollsAmountB[3] += rollB
			if(rollB == 444):
				rollsAmountB[4] += rollB
			if(rollB == 555):
				rollsAmountB[5] += rollB
			if(rollB == 666):
				rollsAmountB[6] += rollB

			if rollA == 1:
				rollsAmountA[rollA] += 111
			if rollA == 2:
				rollsAmountA[rollA] += 222
			if rollA == 3:
				rollsAmountA[rollA] += 333
			if rollA == 4:
				rollsAmountA[rollA] += 444
			if rollA == 5:
				rollsAmountA[rollA] += 555
			if rollA == 6:
				if i+1 == roundAmount:
					rollsAmountA[rollA] += 666
				else:
					rollsAmountA[rollA] += 666*2
					rollB = NormalDiceRoll()
					rollsAmountB[int(rollB/111)] += rollB
					i += 1

			if(rollA != rollB/111):
				if(AViciado):
					AViciado = False
					BViciado = True
				else:
					AViciado = True
					BViciado = False
			i+=1

		else:
			rollA = NormalDiceRoll()
			rollB = random.randint(1, 6)

			if(rollA == 111):
				rollsAmountA[1] += rollA
			if(rollA == 222):
				rollsAmountA[2] += rollA
			if(rollA == 333):
				rollsAmountA[3] += rollA
			if(rollA == 444):
				rollsAmountA[4] += rollA
			if(rollA == 555):
				rollsAmountA[5] += rollA
			if(rollA == 666):
				rollsAmountA[6] += rollA

			if rollB == 1:
				rollsAmountA[rollB] += 111
			if rollB == 2:
				rollsAmountA[rollB] += 222
			if rollB == 3:
				rollsAmountA[rollB] += 333
			if rollB == 4:
				rollsAmountA[rollB] += 444
			if rollB == 5:
				rollsAmountA[rollB] += 555
			if rollB == 6:
				if i+1 == roundAmount:
					rollsAmountA[rollB] += 666
				else:
					rollsAmountA[rollB] += 666*2
					rollA = NormalDiceRoll()
					rollsAmountA[int(rollA/111)] += rollA
					i += 1

			if(rollA != rollB/111):
				if(AViciado):
					AViciado = False
					BViciado = True
				else:
					AViciado = True
					BViciado = False
			i+=1

	return AViciado


def main():
	numero = input()
	if int(numero) > 500:
		numero = 500
	if(pointsInGameWithRoundsCount(numero)):
		print(1)
	else:
		print(2)


if __name__ == "__main__":
	main()
