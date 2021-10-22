import numpy as np

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
	# for digito in number3:
	# 	print(len(number3))
	# 	if number3.index(digito)+1 < len(number3):
	# 		if digito == number3[number3.index(digito)+1]:
	# 			number4 = number4 + ('2'+number3[number3.index(digito)])
	# 		else:
	# 			number4 = number4 + ('1'+number3[number3.index(digito)])

	while(i < len(number3)):
		if i+1 < len(number3):
			if number3[i] == number3[i+1]:
				number4 = number4 + ('2'+number3[i])
				i = i+1
			else:
				number4 = number4 + ('1'+number3[i])
		else:
			number4 = number4 + ('1'+number3[i])
		i = i+1

	return number4


def main():
	print(segundoMembro(3))
	print(terceiroMembro(3))
	print(quartoMembro(3))
	

if __name__ == "__main__":
	main()