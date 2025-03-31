import random

print("Seja bem vindo ao jogo da forca!")
print("Para vencer adivinhe a palavra secreta. Você tem 7 vidas.")
tema = input("Primeiramente escolha um tema: 1 - Animais, 2 - Cores, 3 - Frutas, 4 - Profissoes, 5 - Esportes: ")
if tema == "1":
	lista_palavras = ["cachorro", "gato", "elefante", "leao", "tigre", "girafa", "urso", "raposa", "lobo", "coelho", "jacare", "tartaruga"]
elif tema == "2":
	lista_palavras = ["vermelho", "azul", "verde", "amarelo", "laranja", "roxo", "rosa", "preto", "branco", "cinza"]
elif tema == "3":
	lista_palavras = ["maca", "pera", "morango", "banana", "manga", "uva", "melao", "melancia", "abacaxi", "tangerina", "abacate", "pessego"]
elif tema == "4":
	lista_palavras = ["programador", "medico", "professor", "engenheiro", "arquiteto", "advogado", "jornalista", "designer", "cientista", "contador"]
elif tema == "5":
	lista_palavras = ["futebol", "basquete", "volei", "tenis", "natacao", "ciclismo", "corrida", "rugby", "golfe", "boxe"]
else:
	print("Tema inválido. Tente novamente.")

palavra = random.choice(lista_palavras)
vidas = 7

resposta = []

for i in range(len(palavra)):
	resposta.append("_")
 
	

while vidas > 0:
	if list(palavra) == resposta:
		print(f"Parabéns você venceu! A palavra secreta era {palavra}.")
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
	print(f"Fim do jogo. Tente novamente. A palavra secreta era {palavra}.")
