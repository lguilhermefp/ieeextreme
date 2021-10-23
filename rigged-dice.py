from random import random

def pointsInGameWithRoundsCount(roundAmount):
	i=0
	rollsAmount = [0, 0, 0, 0, 0, 0, 0]
	totalPoints = 0

	while(i<roundAmount):
		roll = round(0.5+6*random())

		if roll == 1:
			rollsAmount[roll] += 111
		if roll == 2:
			rollsAmount[roll] += 222
		if roll == 3:
			rollsAmount[roll] += 333
		if roll == 4:
			rollsAmount[roll] += 444
		if roll == 5:
			rollsAmount[roll] += 555
		if roll == 6:
			if i+1 == roundAmount:
				rollsAmount[roll] += 666
			else:
				rollsAmount[roll] += 666*2
				i += 1
		i+=1


	for r in rollsAmount:
		totalPoints += r

	return totalPoints


def main():
	print(pointsInGameWithRoundsCount(2))
	print(pointsInGameWithRoundsCount(2))
	print(pointsInGameWithRoundsCount(2))
	print(pointsInGameWithRoundsCount(2))
	print(pointsInGameWithRoundsCount(2))
	print(pointsInGameWithRoundsCount(2))
	print(pointsInGameWithRoundsCount(2))
	print(pointsInGameWithRoundsCount(2))
	print(pointsInGameWithRoundsCount(2))
	print(pointsInGameWithRoundsCount(2))
	print(pointsInGameWithRoundsCount(2))
	print(pointsInGameWithRoundsCount(2))


if __name__ == "__main__":
	main()
