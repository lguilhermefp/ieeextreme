import numpy as np

def segundoMembro(number):
	number2 = '1'+str(number)
	return number2


def terceiroMembro(number):
	segundo_membro = segundoMembro(number)
	number2 = list(str(segundo_membro))
	return number2


def main():
	print(segundoMembro(2))
	print(terceiroMembro(2))
	

if __name__ == "__main__":
	main()