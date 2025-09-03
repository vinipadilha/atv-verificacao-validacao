def sao_anagramas(string1, string2):
	pass

def cifra_de_cesar(texto, deslocamento):
	pass

def encontrar_maior_palavra(frase):
	frase = frase.split()
	maior_palavra = ''
	for palavra in frase:
		if len(palavra) > len(maior_palavra):
			maior_palavra = palavra
	return maior_palavra
