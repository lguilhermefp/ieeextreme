import numpy as np

def segundoMembro(number):
	number2 = '1'+str(number)
	return number2


def terceiroMembro(number):
	segundo_membro = segundoMembro(number)
	number2 = list(str(segundo_membro))
	number3 = ''
	
	for digito in number2:
		if digito != number2[number2.index(digito)+1]:
			number3 = number3 + ('1'+number2[number2.index(digito)])

	return number3


def main():
	print(segundoMembro(2))
	print(terceiroMembro(2))
	

if __name__ == "__main__":
	main()