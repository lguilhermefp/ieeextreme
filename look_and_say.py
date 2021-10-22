def membroSeguinteAo(number):
	numberToArray = list(str(number))
	membroSeguinte = ''
	i=0

	while(i < len(numberToArray)):
		if i+1 < len(numberToArray):
			quantidadeEmSequencia = quantidadeDeTermosEmSequencia(i, numberToArray)
			if(termoIgualAoProximo(i, numberToArray)):
				membroSeguinte = membroSeguinte + (str(quantidadeEmSequencia)+numberToArray[i])
				i = i+quantidadeEmSequencia-1
			else:
				membroSeguinte = membroSeguinte + ('1'+numberToArray[i])
		else:
			membroSeguinte = membroSeguinte + ('1'+numberToArray[i])
		i = i+1

	return membroSeguinte


def termoIgualAoProximo(index, array):
	if array[index] == array[index+1]:
		return True


def quantidadeDeTermosEmSequencia(index, array):
	amount = 1
	valueToAnalize = array[index]
	while index+1 < len(array):
		if valueToAnalize == array[index+1]:
			amount += 1
			index += 1
		else:
			break
	return amount


def sequencia(number, size):
	i=0
	while(i<size):
		# print(number)
		number = membroSeguinteAo(number)
		i += 1
	print(number)


def membroN(number):
	sequencia(number, number)


def main():
	number = int(input())
	membroN(number)


if __name__ == "__main__":
	main()