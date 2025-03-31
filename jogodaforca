import random
lista_palavras = ["maca", "pera", "morango", "banana", "manga", "uva", "melao", "melancia", "abacaxi", "tangerina", "abacate", "pessego"]

palavra = random.choice(lista_palavras)
vidas = 7

resposta = []

for i in range(len(palavra)):
	resposta.append("_")
 
print("Seja bem vindo ao jogo da forca!")
	

while vidas > 0:
	if list(palavra) == resposta:
		print("Parabéns você venceu!")
		break  
	print(f"A palavra secreta é	{resposta}. Você tem {vidas} vidas.")
	letra = input("Digite uma letra: ")
	if letra in palavra:
		for i in range(len(palavra)):
			if palavra[i] == letra:
				resposta[i] = letra
	else:
	  vidas -= 1
else:
	print("Fim do jogo. Tente novamente.")
