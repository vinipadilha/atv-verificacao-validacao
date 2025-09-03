def sao_anagramas(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    return sorted(string1) == sorted(string2)


def cifra_de_cesar(texto, deslocamento):
    resultado = ""
    for char in texto:

        if char.isupper():
            resultado += chr((ord(char) - 65 + deslocamento) % 26 + 65)
        elif char.islower():
            resultado += chr((ord(char) - 97 + deslocamento) % 26 + 97)
        else:
            resultado += char
    return resultado


def encontrar_maior_palavra(frase):
	frase = frase.split()
	maior_palavra = ''
	for palavra in frase:
		if len(palavra) > len(maior_palavra):
			maior_palavra = palavra
	return maior_palavra
