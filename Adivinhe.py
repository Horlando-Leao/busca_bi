from random import randint

numero_sorteado = int(randint (1, 10000))
palpite = 0
chutes = 0

while palpite != numero_sorteado:
    palpite = int(input('Seu palpite é: '))
    chutes = chutes + 1

    if palpite == numero_sorteado:
        print("ACERTOU ! Placar %i" %chutes)
    elif palpite < numero_sorteado:
        print('chute um valor maior!')
    else:
         print('chute um valor menor')
print('fim do jogo')
