import random

FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

palavras = 'banana telescopio cachorro martelo girafa hamburger chocolate alimentos biscoito carne supermercado  tia tio pai mae'.split()

def main():
    """ FFunción principal """

    global FORCAIMG
    print('AHORCADO')
    letrasErradas = ''
    letrasAcertadas = ''
    palavraSecreta = geraPalavraAleatória().upper()
    jogando = True

    while jogando:
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
        palpite = recebePalpite(letrasErradas + letrasAcertadas)
        if palpite in palavraSecreta:
            letrasAcertadas += palpite
            if verificaSeGanhou(palavraSecreta, letrasAcertadas):
                print("Exato! A palavra secreta é " +palavraSecreta+'!Você ganhou!!')
                jogando = False

        else:
            letrasErradas += palpite
            if len(letrasErradas) == len(FORCAIMG)-1:
               imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
               print("Você excedeu o seu limite de palpites!")
               print("Depois de "+str(len(letrasErradas))+' letras erradas e '+str(len(letrasAcertadas)), end = ' ')
               print("letras corretas, a palavra era "+palavraSecreta+'.')
               jogando = False

        if not jogando:
            if jogarNovamente():
               letrasErradas = ''
               letrasAcertadas = ''
               jogando = True
               palavraSecreta = geraPalavraAleatória().upper()
                      
def geraPalavraAleatória():
    """ Função que retorna uma strinf a partir da lista de palavras global"""
    global palavras
    return random.choice(palavras)

def imprimeComEspacos(palavra):
    """ Recebe uma strinf ou lista e imprime essa com espaços entre suas letras """
    for letra in palavra:
        print(letra, end = ' ')
    print()

def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    """ Feito a partir da variavel global que contem as imagens do jogo ASCII art"""
    global FORCAIMG
    print(FORCAIMG[len(letrasErradas)] + '\n')

    print("Letras Erradas: ", end = ' ')
    imprimeComEspacos(letrasErradas)

    vazio = '_'*len(palavraSecreta)

    for i in range(len(palavraSecreta)):
        if palavraSecreta[i] in letrasAcertadas:
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:]
       
    imprimeComEspacos(vazio)

def recebePalpite(palpitesFeitos):
    """ Apenas entradas válidas, letras que ele ainda nao utilizou"""

    while True:
        print()
        palpite = input("Adivinhe uma letra. \n").upper()

        if len(palpite) != 1:
            print("Coloque uma única letra. \n")
        elif palpite in palpitesFeitos:
            print("Esta letra já existe, digite outra. \n")
        elif not 'A' <= palpite <= 'Z':
            print("Insiras apenas letras. \n")
        else:
            return palpite
    

def jogarNovamente():

    return input("Voce quer jogar novamente? (sim ou nao) \n").upper().startswith('S')


def verificaSeGanhou(palavraSecreta, letrasAcertadas):
    """Função que verifica se o usuário acertou toas as letras da palavra"""
    ganhou = True

    for letra in palavraSecreta:
        if letra not in letrasAcertadas:
            ganhou = False
            break
    return ganhou


main()

