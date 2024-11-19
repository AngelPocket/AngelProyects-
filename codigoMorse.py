morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'}
texto = input("Escribe un texto para convertirlo a codigo morse o un codigo morse para codificarlo y ponerlo en normal\n ")

codigoo = False
lista_input = texto.split()
lista_palabras = []
for letra, codigo in morse_dict.items():
    if codigo == lista_input[0]:
        codigoo = True

if codigoo:
    for y in lista_input:
        lista_letras = []
        for letra, codigo in morse_dict.items():
            if y == codigo:
               lista_letras.append(letra)
        lista_palabras.append(" ".join(lista_letras))
        
    print(" ".join(lista_palabras))
else:

    for palabra in lista_input:
        word = list(palabra.upper())
        lista_letras = []
        for letra in word:  
            M = morse_dict[letra]
            lista_letras.append(M)
            lista_letras.append(" ")
        lista_palabras.append("".join(lista_letras))
        lista_palabras.append("  ")
        

    print("".join(lista_palabras))      

   
