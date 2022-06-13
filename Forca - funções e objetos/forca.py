# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.tamanho = len(self.word)
        print('Palavra escolhida! Vamos jogar!')
        
    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word:
            return 1
        else:
            return 0
        
    # Método para verificar se o jogo acabou
    def hangman_over(self, erros, letras):
        hide = []
        for i in range(0, self.tamanho):
            hide.append('_')
        for i,l in enumerate(self.word):
            if l in letras:
                hide[i] = l

        if erros >= 6 or '_' not in hide:
            return True
        else:
            return False


        
    # Método para descobrir o jogador ganhou ou não
    def hangman_won(self, erros):
        if erros >= 6:
            return False
        else:
            return True

    # Método para não mostrar a letra no board
    def hide_word(self, letras):
        for l in self.word:
            if l in letras:
                print(l,end='')
            else:
                print('_',end='')
        print('')


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank)-1)].strip()


# Função Main - Execução do Programa
def main():

    # Objeto da classe Hangman com atributo único sendo a palavra escolhida.
    game = Hangman(rand_word())
    print('')
    print(board[0])
    game.hide_word([])

    # listas de letras erradas e corretas
    corretas = []
    erradas = []

    # counter de erros e acertos
    counter_erro = 0

    while True:
        # escolha da letra
        while True:
            letra = str(input('Digite uma letra: '))
            if letra.isalpha() and len(letra.strip()) == 1:
                letra = letra.strip()
                break

        # acertou ou errou letra
        chute = game.guess(letra)

        # executando se letra for correta ou errada
        if chute == 1:
            corretas.append(letra)
            print(f'\nA letra "{letra}" está correta!')
        else:
            counter_erro += 1
            erradas.append(letra)
            print(f'\n A letra "{letra}" está errada!')

        # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
        # print do board
        print(board[counter_erro])

        # print da palavra
        game.hide_word(corretas)


        # print das letras corretas
        print('Letras Corretas:')
        for i in corretas:
            print(i)

        # print das letras erradas
        print('')
        print('Letras Erradas:')
        for i in erradas:
            print(i)
        print('')

        if game.hangman_over(counter_erro, corretas):
            break


        # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won(counter_erro):
        print ('\nParabéns! Você venceu!')
        print(f'Você achou a palavra "{game.word}"!',)
    else:
        print ('\nGame over! Você perdeu.')
        print (f'A palavra era "{game.word}".')
    
    print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
    main()
