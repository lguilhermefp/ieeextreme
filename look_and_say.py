def segundoMembro(number):
	number2 = '1'+str(number)
	return number2


def terceiroMembro(number):
	segundo_membro = segundoMembro(number)
	number2 = list(str(segundo_membro))
	number3 = ''
	
	for digito in number2:
		number3 = number3 + ('1'+number2[number2.index(digito)])

	return number3


def quartoMembro(number):
	terceiro_membro = terceiroMembro(number)
	number3 = list(terceiro_membro)
	number4 = ''
	i=0

	while(i < len(number3)):
		if i+1 < len(number3):
			quantidadeEmSequencia = quantidadeDeTermosEmSequencia(i, number3)
			print(quantidadeEmSequencia)
			if(termoIgualAoProximo(i, number3)):
				number4 = number4 + (str(quantidadeEmSequencia)+number3[i])
				i = i+quantidadeEmSequencia-1
			else:
				number4 = number4 + ('1'+number3[i])
		else:
			number4 = number4 + ('1'+number3[i])
		i = i+1

	return number4


def program(number):
	pass


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


def main():
	print(segundoMembro(3))
	print(terceiroMembro(3))
	print(quartoMembro(3))

if __name__ == "__main__":
	main()